import:py from jaclang.core.llms, OpenAI;

glob llm = OpenAI(model_name="gpt-4o");

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
    info: "Person's Information": str = "Kugesan is a 24 years old and works as an engineer at Jaseci, USA.";
    person = Person(by llm(incl_info=(info)));
    print(f"Their name is {person.name} and she works in {person.employer.location}.");
}
