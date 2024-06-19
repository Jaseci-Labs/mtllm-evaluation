import:py from jaclang.core.llms, OpenAI;
import:py wikipedia;

glob llm = OpenAI(model_name="gpt-4o");

can get_wikipedia_summary(title: str) -> str {
    return wikipedia.summary(title);
}

can get_answer(question: str) -> str by llm(method="ReAct", tools=[get_wikipedia_summary]);

with entry {
    question = "Who is Jason Mars?";
    answer = get_answer(question);
    print("Question:", question);
    print("Answer:", answer);
}
