import:py dspy ;
import:py from pydantic, BaseModel, Field ;
import:py enum ;

with entry {
    llm = dspy.OpenAI(model="gpt-4o");    
    dspy.settings.configure(lm=llm) ;
}

class Personality:enum.Enum: {
    has INTROVERT = "Introvert",
        EXTROVERT = "Extrovert";
}

class Person:BaseModel: {
    has full_name: str = Field(description="Fullname of the Person"),
        yod: int = Field(description="Year of Death"),
        personality: Personality = Field(description="Personality Type");
}

"""Get Person Information use common knowledge."""
class GetPersonInfo:dspy.Signature: {
    has name: str = dspy.InputField(desc="Name of the Person"),
        person: Person = dspy.OutputField();
}

with entry {
    name = "Martin Luther King Jr.";    
    person = dspy.TypedPredictor(GetPersonInfo)(name=name).person;    
    print(f"{person.full_name} was an {person.personality.value} person who died in {person.yod}.");
}
