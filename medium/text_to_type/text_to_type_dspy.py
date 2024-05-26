import dspy
from pydantic import BaseModel, Field

turbo = dspy.OpenAI(model="gpt-3.5-turbo")
dspy.settings.configure(lm=turbo)


class Employer(BaseModel):
    employer_name: str = Field(description="Employer Name")
    location: str = Field(description="Location")


class Person(BaseModel):
    name: str = Field(description="Name")
    age: int = Field(description="Age")
    job: str = Field(description="Job")
    employer: Employer = Field(description="Employer")


class GetPerson(dspy.Signature):
    """Get Person Information."""

    info: str = dspy.InputField(desc="Person Information")
    person: Person = dspy.OutputField()


info = "Alice is a 21 years old and works as an engineer at LMQL Inc in Zurich, Switzerland."
alice = dspy.TypedPredictor(GetPerson)(info=info).person
print(f"Their name is {alice.name} and she works in {alice.employer.location}.")

print(turbo.inspect_history())
