import:py from mtllm.llms, OpenAI;
import:py from PIL, Image;

glob llm = OpenAI(verbose= True, model_name="gpt-4o");

can 
is_path_between_two_dots(image: 'Image to check for path': Image) ->bool 
by llm(method="Chain-of-Thoughts");

with entry {
    print(is_path_between_two_dots(Image.open('true.png')));
    print(is_path_between_two_dots(Image.open('false.png')));
}