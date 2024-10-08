import:py from os {environ}
import:py from mtllm.llms {Ollama}

glob model_name=environ["MODEL_NAME"];
glob llm = Ollama(model_name=model_name, host="http://141.212.106.90:8080", timeout=240, max_tries=1);

can get_answer(question: str) -> int by llm(method="Chain-of-Thoughts");

with entry{
    question = input();
    answer = get_answer(question);
    print(answer);
}

