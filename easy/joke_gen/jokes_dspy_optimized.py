import dspy

llm = dspy.OpenAI(model="gpt-4o")
dspy.settings.configure(lm=llm)


class JokeWithPunchline(dspy.Signature):
    joke: str = dspy.OutputField()
    punchline: str = dspy.OutputField()


tell_a_joke = dspy.Predict(JokeWithPunchline)
pred = tell_a_joke()
print(f"{pred.joke}: {pred.punchline}")
