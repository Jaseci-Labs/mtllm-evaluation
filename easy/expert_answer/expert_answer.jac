import:py from jaclang.core.llms, OpenAI;

glob llm = OpenAI(model_name="gpt-4o");

can 'Find the Expert Profession to answer the given question.'
get_expert(question: 'Question': str) -> 'Expert Profession': str by llm(method="Reason");
can "Get the answer for the question from expert's perspective"
get_answer(question: 'Question': str, expert: 'Expert': str) -> "Expert's Answer": str by llm();

with entry {
    question = "Who is the first Man on Earth?";
    expert = get_expert(question);
    answer = get_answer(question, expert);
    print(f"{expert} says: '{answer}' ");
}
