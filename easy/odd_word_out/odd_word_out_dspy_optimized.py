import dspy

llm = dspy.OpenAI(model="gpt-4o")
dspy.settings.configure(lm=llm)


class OddWordOut(dspy.Signature):
    """Pick the Odd Word Out from the given list of words."""

    options: str = dspy.InputField(desc="Options to pick from")
    reasoning: str = dspy.OutputField(desc="Reasoning")
    odd_word: str = dspy.OutputField(desc="Odd Word")


get_odd_word_out = dspy.Predict(OddWordOut)
pred = get_odd_word_out(
    options=str(["Bentley", "Ferrari", "Lamborghini", "Casio", "Toyota"])
)
print((pred.reasoning, pred.odd_word))
