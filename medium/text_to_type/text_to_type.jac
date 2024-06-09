import:py from mtllm.llms.openai, OpenAICompletion;

glob llm = OpenAICompletion(model_name="gpt-3.5-turbo-instruct");

obj 'Employer'
Employer {
    has employer_name: 'Employer Name': str,
        location: 'Location': str;
}

obj 'Person'
Person {
    has name: 'Name': str,
        age: 'Age': int,
        employer: 'Employer': Employer,
        job: 'Job': str;
}

with entry {
    info: "Person's Information": str = "Alice is a 21 years old and works as an engineer at LMQL Inc in Zurich, Switzerland.";
    person = Person(by llm(incl_info=(info)));
    print(f"Their name is {person.name} and she works in {person.employer.location}.");
}
