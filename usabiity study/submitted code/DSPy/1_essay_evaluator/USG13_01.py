from dsp import LM
import requests
import dspy

llm = Anthropic(model="claude-3-sonnet-20240229")
dspy.configure(lm=llm)

llm = dspy.OpenAI(model="gpt-4o")
dspy.settings.configure(lm=llm)

class EssayEvaluation(dspy.Signature):
    """Evaluate the essay based on the given criterias. Answer questions with short factoid answers."""
    entered_essay = dspy.InputField()
    evaluation_criteria = dspy.InputField()
    grade_range = dspy.InputField()

    grade = dspy.OutputField(desc="Grade among A,B,C,S,F based on the evaluation")
    remark = dspy.OutputField(desc="small remark with important points.")

class CoT(dspy.Module):
    def __init__(self):
        super().__init__()
        self.prog = dspy.ChainOfThought(EssayEvaluation)

    def forward(self, entered_essay, evaluation_criteria, grade_range):
        return self.prog(entered_essay=entered_essay, evaluation_criteria=evaluation_criteria, grade_range=grade_range)

c = CoT()

#Criterias for the evaluation can be given here
evaluation_criteria = """
    clarity (0-10 marks),
    coherency (0-10 marks),
    grammer (0-10 marks),
    """
grade_ranges = "A (if marks 100-75), B (if marks 74-65), C (if marks 64-55), S (if marks 54-35), F (if marks 34-0)"

entered_essay = """The global power crisis is caused by high energy demand, old infrastructure, and reliance on fossil fuels.
            This crisis results in blackouts, higher costs for businesses, and problems for healthcare and education.
             To fix this, we need to use more renewable energy like solar and wind, update infrastructure, and use energy
             more efficiently. Better governance and regulations can help manage the crisis and attract investments for
             a stable energy future."""
response = c.forward(entered_essay, evaluation_criteria, grade_ranges)

print("Grade = ", response['grade'])
print("Remark = ", response['remark'])
