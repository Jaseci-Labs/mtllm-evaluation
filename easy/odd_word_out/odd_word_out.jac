import:py from jaclang.core.llms, BaseLLM;

obj model :BaseLLM: {
    can init(output_str: str) {
        self.output_str = output_str;
    }

    can __infer__(meaning_in: str, **kwargs: dict) {
        print(meaning_in);
        return f"[Output] {self.output_str}";
    }
}

glob llm = model(output_str="A");

glob examples: 'Examples for Picking Odd Word out' : list[dict] = [
    {
        "OPTIONS": ["skirt", "dress", "pen", "jacket"],
        "REASONING": "skirt is clothing, dress is clothing, pen is an object, jacket is clothing.",
        "RESULT": "pen"
    },
    {
        "OPTIONS": ["Spain", "France", "German", "England", "Singapore"],
        "REASONING": "Spain is a country, France is a country, German is a language, ...",
        "RESULT": "German"
    }
];

can 'Pick the Odd word out'
pick_odd_word_out_v1(options: 'Options to pick from': list[str]) -> 'Result' :str by llm(incl_info=(examples));

can 'Pick the Odd word out'
pick_odd_word_out_v2(options: 'Options to pick from' :list[str]) -> 'OPTIONS, REASONING & RESULT' :dict by llm(reason=True,incl_info=(examples));

with entry {
    options = ["Bentley", "Ferrari", "Lamborghini", "Casio", "Toyota"];
    # print(pick_odd_word_out_v1(options)); # Casio
    print(pick_odd_word_out_v2(options)); # {"OPTIONS": ["Bentley", "Ferrari", "Lamborghini", "Casio", "Toyota"], "REASONING": "Bentley is a car, Ferrari is a car, Lamborghini is a car, Casio is a watch, Toyota is a car.", "RESULT": "Casio"}
}