import dspy
from dspy.teleprompt import BootstrapFewShot
from pydantic import BaseModel, Field
import wikipedia

llm = dspy.OpenAI(model="gpt-3.5-turbo-instruct")
dspy.settings.configure(lm=llm)


class ThoughtActionObservation(BaseModel):
    thought: str = Field(description="Thought")
    action_type: str = Field(description="Action Type (Search or Finish)")
    action_info: str = Field(description="Search Term or Final Answer")
    observation: str = Field(description="Observation")


example = {
    "question": "What is the elevation range for the area that the eastern sector of the Colorado orogeny extends into?",
    "prev_thought_action_observation": [
        ThoughtActionObservation(
            thought="I need to search Colorado orogeny, find the area that the eastern sector of the Colorado ...",
            action_type="Search",
            action_info="Colorado orogeny",
            observation="The Colorado orogeny was an episode of mountain building (an orogeny) ...",
        ),
        ThoughtActionObservation(
            thought="It does not mention the eastern sector. So I need to look up eastern sector.",
            action_type="Search",
            action_info="eastern sector of the Colorado orogeny",
            observation="The eastern sector of the Colorado orogeny extends into the High Plains.... ",
        ),
    ],
    "next_thought": "High Plains rise in elevation from around 1,800 to 7,000 ft, so the answer is 1,800 to 7,000 ft",
    "next_action_type": "Finish",
    "next_action_info": "1,800 to 7,000 ft",
}

dataset = [
    dspy.Example(
        question=example["question"],
        prev_thought_action_observation=example["prev_thought_action_observation"],
        next_thought=example["next_thought"],
        next_action_type=example["next_action_type"],
        next_action_info=example["next_action_info"],
    ).with_inputs("question", "prev_thought_action_observation")
]


class GetNextThoughtAction(dspy.Signature):
    """Get Next Thought, Action"""

    question: str = dspy.InputField(desc="Question")
    prev_thought_action_observation: list[ThoughtActionObservation] = dspy.InputField(
        desc="Previous Thoughts, Actions, Observations"
    )
    next_thought: str = dspy.OutputField(desc="Next Thought")
    next_action_type: str = dspy.OutputField(desc="Next Action Type (Search or Finish)")
    next_action_info: str = dspy.OutputField(
        desc="Next Action Info (Search Term or Final Answer)"
    )


class GetNextThoughtActionModule(dspy.Module):
    def __init__(self):
        super().__init__()
        self.generate_answer = dspy.TypedPredictor(GetNextThoughtAction)

    def forward(
        self,
        question: str,
        prev_thought_action_observation: list[ThoughtActionObservation],
    ):
        pred = self.generate_answer(
            question=question,
            prev_thought_action_observation=prev_thought_action_observation,
        )
        return dspy.Prediction(
            next_thought=pred.next_thought,
            next_action_type=pred.next_action_type,
            next_action_info=pred.next_action_info,
        )


get_next_thought_action = BootstrapFewShot().compile(
    GetNextThoughtActionModule(), trainset=dataset
)


def get_answer(question: str) -> str:
    """Get Answer to the Question"""
    prev_info = []
    while len(prev_info) < 100:
        pred = get_next_thought_action(
            question=question, prev_thought_action_observation=prev_info[-3:]
        )
        if pred.next_action_type == "Search":
            obs = wikipedia.summary(pred.next_action_info)
        elif pred.next_action_type == "Finish":
            return pred.next_action_info
        prev_info.append(
            ThoughtActionObservation(
                thought=pred.next_thought,
                action_type=pred.next_action_type,
                action_info=pred.next_action_info,
                observation=obs,
            )
        )
    return "I am sorry, I could not find the answer."


question = "Where is Apple Headquaters located?"
answer = get_answer(question)
print("Question: ", question)
print("Answer: ", answer)
question = "Who is Jason Mars?"
answer = get_answer(question)
print("Question: ", question)
print("Answer: ", answer)
