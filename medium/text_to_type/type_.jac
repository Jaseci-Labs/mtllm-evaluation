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

glob llm = model(output_str="Person(name='Claude', age=2, employer=Employer(employer_name='Anthropic', location='San Francisco'), job='AI assistant')");


obj 'Employer'
Employer {
    has employer_name: 'Employer Name' :str,
        location: 'Location' :str;
}

obj 'Person'
Person {
    has name: 'Name': str,
        age: 'Age' :int,
        employer: 'Employer': Employer,
        job: 'Job' :str;
}

with entry {
    info: "Person's Information" :str = "Alice is a 21 years old and works as an engineer at LMQL Inc in Zurich, Switzerland.";
    person = Person(by llm(incl_info=(info)));
    print(f"Their name is {person.name} and she works in {person.employer.location}.");
}