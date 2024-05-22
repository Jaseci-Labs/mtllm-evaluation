import:py from jaclang.core.llms, BaseLLM;

obj model :BaseLLM: {
    can init(output_str: str) {
        self.output_str = output_str;
    }

    can __infer__(meaning_in: str, **kwargs: dict) {
        print(meaning_in);
        return f"[Output] {self.output_str}";
    }
}

glob llm = model(output_str="AI/ML Researcher or Engineer");

can 'Finds the best professional to answer the given question'
get_expert(question: 'Question': str)-> 'Expert Profession': str by llm(reason=True);

can "Get the answer for the question from expert's perspective"
get_answer(question:'Question': str, expert: 'Expert': str)-> "Expert's Answer": str by llm(temperature=1.0);

with entry{
    question = "What are Large Language Models?";
    expert = get_expert(question);
    answer = get_answer(question, expert);
    print(f"For instance, {expert} would answer '{answer}' for the question '{question}'");
}