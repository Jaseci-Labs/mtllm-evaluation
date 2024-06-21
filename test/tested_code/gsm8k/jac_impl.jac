import:py from os, environ;
import:py from mtllm.llms, OpenAI;

glob model_name=environ["MODEL_NAME"];
glob llm = OpenAI(verbose=True, model_name=model_name);

can get_answer(question: str) -> int by llm(method="Chain-of-Thoughts");

with entry{
    question = "Weng earns $12 an hour for babysitting. Yesterday, she just did 50 minutes of babysitting. How much did she earn?";
    answer = get_answer(question);
    print(answer);
}
