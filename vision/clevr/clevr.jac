import:py from mtllm.llms, OpenAI;
import:py from mtllm, Image;

glob llm = OpenAI(model_name="gpt-4o");

can get_answer(img: Image, question: str) -> str by llm();

with entry {
    img = Image("image.png");
    question = "How many objects in this picture?";
    get_answer(img, question);
}