import dspy
from pydantic import BaseModel, Field

turbo = dspy.OpenAI(model="gpt-4o")
dspy.settings.configure(lm=turbo)


class get_answer(dspy.Signature):
    "Provide the Answer for the Given Question (A-F)"
    question: str = dspy.InputField(description="Question")
    choices: dict = dspy.InputField(description="Answer Choices")
    answer: str = dspy.OutputField(description="Answer (A-F)")


gen_answer = dspy.ChainOfThought(get_answer)  # FIXME
ans = gen_answer(
    question="It was Sept. 1st, 2021 a week ago. What is the date 10 days ago in MM/DD/YYYY?",
    choices={
        "A": "08/29/2021",
        "B": "08/28/2021",
        "C": "08/29/1925",
        "D": "08/30/2021",
        "E": "05/25/2021",
        "F": "09/19/2021",
    },
)
print(ans)
