import dspy
import dspy.teleprompt

turbo = dspy.OpenAI(model="gpt-3.5-turbo")
dspy.settings.configure(lm=turbo)

examples: list[tuple[str, str]] = [
    ("How does a penguin build its house?", "Igloos it together."),
    ("Which knight invented King Arthur's Round Table?", "Sir Cumference."),
]

dataset = [
    dspy.Example(joke=example[0], punchline=example[1]).with_inputs()
    for example in examples
]


class JokeWithPunchline(dspy.Signature):
    """Tell a joke with a punchline."""

    joke: str = dspy.OutputField(desc="Joke")
    punchline: str = dspy.OutputField(desc="Punchline")


class JokeWithPunchlineModule(dspy.Module):
    def __init__(self):
        super().__init__()
        self.generate_answer = dspy.predictor(JokeWithPunchline)

    def forward(self):
        pred = self.generate_answer()
        return dspy.Prediction(joke=pred.joke, punchline=pred.punchline)


tell_a_joke = dspy.teleprompt.BootstrapFewShot().compile(
    JokeWithPunchlineModule(), trainset=dataset
)
pred = tell_a_joke()
print(f"{pred.joke}: {pred.punchline}")
