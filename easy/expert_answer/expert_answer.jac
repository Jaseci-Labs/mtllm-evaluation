import:py from mtllm.llms, Ollama;

glob llm = Ollama(host="http://52.23.242.52:11343");

can 'Find the Expert Profession to answer the given question.'
get_expert(question: 'Question': str) -> 'Expert Profession': str by llm(method="Reason");
can "Get the answer for the question from expert's perspective"
get_answer(question: 'Question': str, expert: 'Expert': str) -> "Expert's Answer": str by llm();

with entry {
    question = "What are Large Language Models?";
    expert = get_expert(question);
    answer = get_answer(question, expert);
    print(f"{expert} says: '{answer}' ");
}
