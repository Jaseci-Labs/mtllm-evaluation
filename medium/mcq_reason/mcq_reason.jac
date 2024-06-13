import:py from jaclang.core.llms, OpenAI;

glob llm = OpenAI(model_name="gpt-4o");

can 'Provide the Answer for the Given Question (A-F)'
get_answer(question: 'Question': str, choices: 'Answer Choices': dict) -> 'Answer (A-F)': str
by llm(method="Chain-of-Thoughts", temperature=0.0);

with entry {
    question: str = "2*1012+1/2 = ?";
    choices: dict = {
        "A": "1023",
        "B": "2024.5",
        "C": "2024",
        "D": "1024",
        "E": "2023.5",
        "F": "1023.5"
    };
    print(get_answer(question, choices));
}
