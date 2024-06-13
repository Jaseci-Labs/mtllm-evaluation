import dspy

llm = dspy.OpenAI(model="gpt-4o")
dspy.settings.configure(lm=llm)


class get_answer(dspy.Signature):
    "Provide the Answer for the Given Question (A-F)"
    question: str = dspy.InputField(description="Question")
    choices: str = dspy.InputField(description="Answer Choices")
    answer: str = dspy.OutputField(description="Answer (A-F)")


gen_answer = dspy.ChainOfThought(get_answer)
question = "2*1012+1/2 = ?"
choices = "(A) 1023 (B) 2024.5 (C) 2024 (D) 1024 (E) 2023.5 (F) 1023.5"
ans = gen_answer(question=question, choices=choices)
print(ans.rationale, ans.answer)
