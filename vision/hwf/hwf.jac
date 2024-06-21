import:py from mtllm.llms, OpenAI;
import:py from mtllm, Image;

glob llm = OpenAI(verbose=True, model_name="gpt-4o");

can 'Solve the given Math Question'
solve_math(question: 'Mathematic Formula': Image) -> str by llm(method="Chain-of-Thoughts");

with entry {
    print(solve_math(Image("image.png")));
}