import dspy
from pydantic import BaseModel, Field
import enum

llm = dspy.OpenAI(model="gpt-4o")
dspy.settings.configure(lm=llm)


class Personality(enum.Enum):
    INTROVERT = "Introvert"
    EXTROVERT = "Extrovert"


class Person(BaseModel):
    full_name: str = Field(description="Fullname of the Person")
    yod: int = Field(description="Year of Death")
    personality: Personality = Field(description="Personality Type")


class GetPersonInfo(dspy.Signature):
    """Get Person Information use common knowledge."""

    name: str = dspy.InputField(desc="Name of the Person")
    person: Person = dspy.OutputField()


name = "Martin Luther King Jr."
person = dspy.TypedPredictor(GetPersonInfo)(name=name).person
print(
    f"{person.full_name} was an {person.personality.value} person who died in {person.yod}."
)
