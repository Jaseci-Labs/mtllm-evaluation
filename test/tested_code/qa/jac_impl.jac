import:py from jaclang.core.llms, Ollama, OpenAI;
glob llm = OpenAI();
can answerquestion(question: str) -> 'answer': str by llm();

with entry{
    question = input();
    answer = answerquestion(question);
    print(answer);
}
