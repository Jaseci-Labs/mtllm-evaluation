import:py from jaclang.core.llms, Anthropic;

glob llm = Anthropic();

can 'Find the Expert Profession to answer the given question.'
get_expert(question: 'Question': str) -> 'Expert Profession': str by llm(reason=True);
can "Get the answer for the question from expert's perspective"
get_answer(question: 'Question': str, expert: 'Expert': str) -> "Expert's Answer": str by llm();

with entry {
    question = "What are Large Language Models?";
    expert = get_expert(question);
    answer = get_answer(question, expert);
    print(f"{expert} says: '{answer}' ");
}
