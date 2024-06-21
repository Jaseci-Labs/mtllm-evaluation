import lmql
from dataclasses import dataclass


@dataclass
class Person:
    full_name: str
    yod: int
    personality: str


@lmql.query()
def personality_finder(name: str) -> Person:
    """lmql
    "Personality should be Introvert or Extrovert\n"
    "Get the Person object for {name}.\n"
    "Structured: [PERSON_DATA]\n" where type(PERSON_DATA) is Person
    return PERSON_DATA
    """


person = personality_finder("Martin Luther King Jr.")
print(
    f"{person.full_name} was an {person.personality} person who died in {person.yod}."
)
