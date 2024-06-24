import:py from mtllm.llms, OpenAI;
import:py from mtllm, Image;

glob llm = OpenAI(model_name="gpt-4o");

can 'Check whether the  2 dots are connected by a path'
is_connected(image: Image) -> bool by llm(method="Chain-of-Thoughts");

with entry {
    print(is_connected(Image('true.png')));
    print(is_connected(Image('false.png')));
}