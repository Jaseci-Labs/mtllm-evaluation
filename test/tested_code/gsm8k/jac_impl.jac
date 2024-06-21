import:py from os, environ;
import:py from jaclang.core.llms, Ollama, OpenAI;
glob model_name=environ["MODEL_NAME"];
glob llm = OpenAI(model_name=model_name);
can answerquestion(question: str) -> 'answer': int by llm(method="Chain-of-Thoughts");

with entry{
    question = input();
    answer = answerquestion(question);
    print(answer);
}
