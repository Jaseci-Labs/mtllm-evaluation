import:py from mtllm.llms, OpenAI;

glob llm = OpenAI(model_name="gpt-4o");

obj Employer {
    has employer_name: str, location: str;
}

obj Person {
    has name: str, age: int, employer: Employer, job: str;
}

with entry {
    info: str = "Alice is a 21 years old and works as an engineer at LMQL Inc in Zurich, Switzerland.";
    person = Person(by llm(incl_info=(info)));
    print(f"Their name is {person.name} and she works in {person.employer.location}.");
}
