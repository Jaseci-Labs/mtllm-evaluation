import lmql
from dataclasses import dataclass
import enum


class Personality(enum.Enum):
    INTROVERT = "Introvert"
    EXTROVERT = "Extrovert"


@dataclass
class Person:
    full_name: str
    yod: int
    personality: str


@lmql.query()
def personality_finder(name: str) -> Person:
    """lmql
    "Get the Person object for {name}.\n"
    "Structured: [PERSON_DATA]\n" where type(PERSON_DATA) is Person
    return PERSON_DATA
    """


person = personality_finder("Martin Luther King Jr.")
print(
    f"{person.full_name} was an {person.personality} person who died in {person.yod}."
)


"""
# Expected Output: Martin Luther King Jr. was an Introvert person who died in 39.
# Current Output: Martin Luther King Jr. was an inspirational person who died in 39.

The output is not as expected. The model fails to predict the personality type correctly.
Additionally, when the personality attribute type is specified as Personality, 
it results in the following error:

  File "/home/acer/miniconda3/lib/python3.12/site-packages/lmql/lib/types.py", line 12, in type_schema
    return {f.name: type_schema(f.type) for f in fields(t)}
                    ^^^^^^^^^^^^^^^^^^^
  File "/home/acer/miniconda3/lib/python3.12/site-packages/lmql/lib/types.py", line 21, in type_schema
    assert False, "not a supported type " + str(t)
AssertionError: not a supported type <enum 'Personality'>
"""
