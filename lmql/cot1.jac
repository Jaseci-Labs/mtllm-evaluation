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

can 'Provide the Answer for the Given Question (A-F)'
get_answer(question: 'Question': str, choices: 'Answer Choices': dict) 
-> 'Answer (A-F)': str by llm(reason=True);

with entry {
    question: str = "It was Sept. 1st, 2021 a week ago. What is the date 10 days ago in MM/DD/YYYY?";
    choices: dict = {
        "A": "08/29/2021",
        "B": "08/28/2021",
        "C": "08/29/1925",
        "D": "08/30/2021",
        "E": "05/25/2021",
        "F": "09/19/2021"
    };
    print(get_answer(question, choices));
}
