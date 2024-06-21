import:py from mtllm.llms, OpenAI;
import:py from mtllm, Image;

glob llm = OpenAI(model_name="gpt-4o");

can get_sum_2(digit_1: Image, digit_2: Image) -> int by llm();
can get_sum_3(digit_1: Image, digit_2: Image, digit_3: Image) -> int by llm();
can get_sum_4(digit_1: Image, digit_2: Image, digit_3: Image, digit_4: Image) -> int by llm();
can less_than(digit_1: Image, digit_2: Image) -> 'digit_1 < digit_2': bool by llm();
can not_3_or_4(digit: Image) -> 'digit != 3 and digit != 4': bool by llm();
can count_3(digit_1: Image, digit_2: Image, digit_3: Image, digit_4: Image, digit_5: Image,
            digit_6: Image, digit_7: Image, digit_8: Image) -> 'Number of times Number 3 is Represented': int by llm();
can count_3_or_4(digit_1: Image, digit_2: Image, digit_3: Image, digit_4: Image, digit_5: Image,
                 digit_6: Image, digit_7: Image, digit_8: Image) -> 'Number of Times Number 3 or 4 is represented': int by llm();


with entry {
    digit_1 = Image("images/digit_1.png");
    digit_2 = Image("images/digit_2.png");
    digit_3 = Image("images/digit_3.png");
    digit_4 = Image("images/digit_4.png");
    digit_5 = Image("images/digit_5.png");
    digit_6 = Image("images/digit_6.png");
    digit_7 = Image("images/digit_7.png");
    digit_8 = Image("images/digit_8.png");

    print("Sum of 2 numbers: ", get_sum_2(digit_2, digit_3));
    print("Sum of 3 numbers: ", get_sum_3(digit_2, digit_3, digit_4));
    print("Sum of 4 numbers: ", get_sum_4(digit_2, digit_3, digit_4, digit_5));
    print("Is digit_1 less than digit 2: ", less_than(digit_4, digit_5));
    print("Is digit not 3 or 4: ", not_3_or_4(digit_6));
    print("Count of 3: ", count_3(digit_1, digit_2, digit_3, digit_4, digit_5, digit_6, digit_7, digit_8));
    print("Count of 3 or 4: ", count_3_or_4(digit_1, digit_2, digit_3, digit_4, digit_5, digit_6, digit_7, digit_8));
}