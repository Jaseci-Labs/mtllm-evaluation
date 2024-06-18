import:py from jaclang.core.llms, OpenAI;
import:py wikipedia;

glob llm = OpenAI(model_name="gpt-4o");

enum ActionType {
    Search,
    Finish
}

obj ThoughtAction {
    has thought: str,
        action_type: ActionType,
        action_info: str;
}

obj ThoughtActionObservation {
    has thought_action: ThoughtAction,
        observation: str;
}

glob example: dict = {
    "question": "What is the elevation range for the area that the eastern sector of the Colorado orogeny extends into?",
    "react_process": [
        ThoughtActionObservation(
            thought_action=ThoughtAction(
               thought="I need to search Colorado orogeny, find the area that the eastern sector of the Colorado ...",
                action_type=ActionType.Search,
                action_info="Colorado orogeny"
            ),
            observation="The Colorado orogeny was an episode of mountain building (an orogeny) ..."
        ),
        ThoughtActionObservation(
            thought_action=ThoughtAction( 
                thought="It does not mention the eastern sector. So I need to look up eastern sector.",
                action_type=ActionType.Search,
                action_info="eastern sector of the Colorado orogeny"
            ),
            observation="The eastern sector of the Colorado orogeny extends into the High Plains.... "
        )
    ],
    "final_thought_action": ThoughtAction(
        thought="High Plains rise in elevation from around 1,800 to 7,000 ft, so the answer is 1,800 to 7,000 ft",
        action_type=ActionType.Finish,
        action_info="1,800 to 7,000 ft"
    )
};

can get_next_thought_action(question: str, prev_thought_action_observation: list[ThoughtActionObservation])
-> ThoughtAction by llm(incl_info=(example));

"""Get Answer to the Question"""
can get_answer(question: str) -> str {
    prev_info = [];
    while len(prev_info) < 100 {
        next_thought_action = get_next_thought_action(question, prev_info[-3:]);
        print(next_thought_action);
        if next_thought_action.action_type == ActionType.Search {
            obs= wikipedia.summary(next_thought_action.action_info);
            prev_info.append(ThoughtActionObservation(thought_action=next_thought_action, observation=obs));
            print(obs);
        }
        if next_thought_action.action_type == ActionType.Finish{
            return next_thought_action.action_info;
        }
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
