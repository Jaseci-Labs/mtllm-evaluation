import dspy
import time

import dspy.teleprompt

start_time = time.time()

turbo = dspy.OpenAI(model="gpt-3.5-turbo")
dspy.settings.configure(lm=turbo)

examples: dict[str, str] = {
    "sea otter": "loutre de mer",
    "peppermint": "menthe poivrée",
    "plush giraffe": "girafe en peluche",
}

dataset = [
    dspy.Example(english_word=english_word, translation=translation).with_inputs(
        "english_word"
    )
    for english_word, translation in examples.items()
]

print(dataset)


class Translation(dspy.Signature):
    """Translate the given English word"""

    english_word: str = dspy.InputField(desc="English word to translate")
    translation: str = dspy.OutputField(desc="Translation")


class TranslationModule(dspy.Module):
    def __init__(self):
        super().__init__()
        self.generate_answer = dspy.predictor(Translation)

    def forward(self, english_word: str):
        prediction = self.generate_answer(english_word=english_word)
        return dspy.Prediction(translation=prediction.translation)


translate = dspy.teleprompt.BootstrapFewShot().compile(
    TranslationModule(), trainset=dataset
)
pred = translate(english_word="cheese")
print(pred.translation)
print("Time taken:", time.time() - start_time, "seconds")
