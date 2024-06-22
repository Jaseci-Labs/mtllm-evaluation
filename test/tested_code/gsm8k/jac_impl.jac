import:py from os, environ;
import:py from mtllm.llms, OpenAI;

glob model_name=environ["MODEL_NAME"];
glob llm = OpenAI(verbose=True, model_name=model_name);

can get_answer(question: str) -> int by llm(method="Chain-of-Thoughts");

with entry{
    question = input();
    answer = get_answer(question);
    print(answer);
}
