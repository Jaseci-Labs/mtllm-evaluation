import lmql
from dataclasses import dataclass


@dataclass
class Employer:
    employer_name: str
    location: str


@dataclass
class Person:
    name: str
    age: int
    employer: Employer
    job: str


@lmql.query
def person_data():
    """lmql
    "Alice is a 21 years old and works as an engineer at LMQL Inc in Zurich, Switzerland.\n"
    "Structured: [PERSON_DATA]\n" where type(PERSON_DATA) is Person
    return PERSON_DATA
    """


alice = person_data()
print(alice)
print(f"Their name is {alice.name} and she works in {alice.employer.location}.")
