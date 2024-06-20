import:py from jaclang.core.llms, OpenAI;
import:py from PIL, Image;

glob llm = OpenAI(model_name="gpt-4o");

can get_sum_2(digit_1: Image, digit_2: Image) -> int by llm();
can get_sum_3(digit_1: Image, digit_2: Image, digit_3: Image) -> int by llm();
can get_sum_4(digit_1: Image, digit_2: Image, digit_3: Image, digit_4: Image) -> int by llm();
can less_than(digit_1: Image, digit_2: Image) -> 'digit_1 < digit_2': bool by llm();
can not_3_or_4(digit: Image) -> 'digit != 3 and digit != 4': bool by llm();
can count_3(digit_1: Image, digit_2: Image, digit_3: Image, digit_4: Image, digit_5: Image,
            digit_6: Image, digit_7: Image, digit_8: Image) -> int by llm();
can count_3_or_4(digit_1: Image, digit_2: Image, digit_3: Image, digit_4: Image, digit_5: Image,
                 digit_6: Image, digit_7: Image, digit_8: Image) -> int by llm();