import:py from os {environ}
import:py from mtllm.llms {OpenAI}

glob llm = OpenAI(model_name='gpt-4o');

can get_answer(question: str) -> int by llm(method="Chain-of-Thoughts");

with entry{
    question = input();
    answer = get_answer(question);
    print(answer);
}