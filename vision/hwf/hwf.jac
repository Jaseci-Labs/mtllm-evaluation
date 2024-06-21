import:py from mtllm.llms, OpenAI;
import:py from mtllm, Image;

glob llm = OpenAI(model_name="gpt-4o");

can get_answer(question: Image) -> str by llm(method="Chain-of-Thoughts");

with entry {
    print(get_answer(Image("image.png")));
}