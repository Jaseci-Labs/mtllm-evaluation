import:py dspy ;
import:py from pydantic, BaseModel, Field ;

with entry {
    llm = dspy.OpenAI(model="gpt-4o");    
    dspy.settings.configure(lm=llm) ;
}

class Employer : BaseModel : {
    with entry {
        employer_name: str = Field(description="Employer Name");    
        location: str = Field(description="Location");
    }
}

class Person : BaseModel : {
    with entry {
        name: str = Field(description="Name");    
        age: int = Field(description="Age");    
        job: str = Field(description="Job");    
        employer: Employer = Field(description="Employer");
    }
}

"""Get Person Information."""
class GetPerson : dspy.Signature : {
    with entry {
        info: str = dspy.InputField(desc="Person Information");    
        person: Person = dspy.OutputField();
    }
}

with entry {
    info = "Alice is a 21 years old and works as an engineer at LMQL Inc in Zurich, Switzerland.";    
    alice = dspy.TypedPredictor(GetPerson)(info=info).person;    
    print(
        f"{"Their name is "}{alice.name}{" and she works in "}{alice.employer.location}{"."}"
    ) ;
}

