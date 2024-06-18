import dspy

llm = dspy.OpenAI(model="gpt-4o")
dspy.settings.configure(lm=llm)


class JokeWithPunchline(dspy.Signature):
    """Tell a joke with a punchline."""

    joke: str = dspy.OutputField(desc="Joke")
    punchline: str = dspy.OutputField(desc="Punchline")


tell_a_joke = dspy.Predict(JokeWithPunchline)
pred = tell_a_joke()
print(f"{pred.joke}: {pred.punchline}")
