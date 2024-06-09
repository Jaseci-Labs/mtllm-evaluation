import:py from mtllm.llms.openai, OpenAICompletion;
import:py wikipedia;

glob llm = OpenAICompletion(model_name="gpt-3.5-turbo-instruct");

obj 'Thought, Action Observation'
ThoughtActionObservation {
    has thought: 'Thought': str,
        action_type: 'Action Type (Search or Finish)': str,
        action_info: 'Search Term or Final Answer': str,
        observation: 'Observation': str;
}

glob example: 'QA example with Thoughts and Actions': dict = {
    "question": "What is the elevation range for the area that the eastern sector of the Colorado orogeny extends into?",
    "prev_thought_action_observation": [
        ThoughtActionObservation(
            thought="I need to search Colorado orogeny, find the area that the eastern sector of the Colorado ...",
            action_type="Search",
            action_info="Colorado orogeny",
            observation="The Colorado orogeny was an episode of mountain building (an orogeny) ..."
        ),
        ThoughtActionObservation(
            thought="It does not mention the eastern sector. So I need to look up eastern sector.",
            action_type="Search",
            action_info="eastern sector of the Colorado orogeny",
            observation="The eastern sector of the Colorado orogeny extends into the High Plains.... "
        )
    ],
    "next_thought": "High Plains rise in elevation from around 1,800 to 7,000 ft, so the answer is 1,800 to 7,000 ft",
    "next_action_type": "Finish",
    "next_action_info": "1,800 to 7,000 ft"
};

can 'Get Next Thought Action'
get_next_thought_action(question: 'Question': str, 
            prev_thought_action_observation: 'Previous Thoughts, Actions and Observations': list[ThoughtActionObservation])
-> 'Thought, Action Type, Action Info': tuple(str, str, str) by llm(incl_info=(example));

"""Get Answer to the Question"""
can get_answer(question: str) -> str {
    prev_info = [];
    while len(prev_info) < 100 {
        (thought, action_type, action_info) = get_next_thought_action(question, prev_info[-3:]);
        print(thought, action_type, action_info);
        if action_type == "Search" {
            obs= wikipedia.summary(action_info);
            print(obs);
        }
        if action_type == "Finish" {
            return action_info;
        }
        prev_info.append(ThoughtActionObservation(thought=thought, action_type=action_type, action_info=action_info, 
                                                observation=obs));
    }
}

with entry {
    question = "Where is Apple Headquaters located?";
    answer = get_answer(question);
    print("Question: ", question);
    print("Answer: ", answer);
    question = "Who is Jason Mars?";
    answer = get_answer(question);
    print("Question: ", question);
    print("Answer: ", answer);
}
