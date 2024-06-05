import:py from jaclang.core.llms, OpenAI;

glob llm = OpenAI(model_name="gpt-4o");

can 'Provide the Answer for the Given Question (A-F)'
get_answer(question: 'Question': str, choices: 'Answer Choices': dict) -> 'Answer (A-F)': str
by llm(method="Chain-of-Thoughts", temperature=0.0);

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
