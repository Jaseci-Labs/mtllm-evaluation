import:py from mtllm.llms, OpenAI;

glob llm = OpenAI(model_name="gpt-4o");

can get_suitable_expert(question: str) -> str by llm(method="Reason");
can get_answer_of_expert(question: str, expert: str) -> str by llm();

with entry {
    question = "What are Large Language Models?";
    expert = get_suitable_expert(question);
    answer = get_answer_of_expert(question, expert);
    print(f"{expert} says: '{answer}' ");
}
