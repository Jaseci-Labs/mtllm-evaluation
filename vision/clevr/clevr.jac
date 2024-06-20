import:py from jaclang.core.llms, OpenAI;
import:py from PIL, Image;

glob llm = OpenAI(model_name="gpt-4o");

can get_answer(img: Image, question: str) -> str by llm();