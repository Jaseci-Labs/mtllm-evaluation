import dspy

# This is the configuration of Anthropic Claude-3 model. The code is included in the following google colab link.
# https://colab.research.google.com/drive/1xooazoy49vPspFrtNGKgbATCfpAJUji7?usp=sharing
# from model_config.anthropic import Claude

# claude_model = Claude(model="claude-3-sonnet-20240229")
# dspy.configure(lm=claude_model)

llm = dspy.OpenAI(model="gpt-4o")
dspy.settings.configure(lm=llm)


# Evaluation Template
class EssayEvaluation(dspy.Signature):
    """Evaluate the essay based on the given criterias. Answer questions with short factoid answers."""
    entered_essay = dspy.InputField()
    evaluation_criteria = dspy.InputField()
    grade_range = dspy.InputField()

    grade = dspy.OutputField(desc="Grade among A,B,C,S,F based on the evaluation")
    remark = dspy.OutputField(desc="small remark with important points.")




class COT(dspy.Module):
    def __init__(self):
        super().__init__()
        self.prog = dspy.ChainOfThought(EssayEvaluation)

    def forward(self, entered_essay, evaluation_criteria, grade_range):
        return self.prog(entered_essay=entered_essay, evaluation_criteria=evaluation_criteria, grade_range=grade_range)
    

c = COT()


# Sample information
evaluation_criteria = """
    Thesis Statement (0-10 marks), 
    Clarity of Argument (0-10 marks), 
    Organization (0-10 marks), 
    Supporting Evidence (0-10 marks), 
    Analysis and Critical Thinking (0-10 marks), 
    Use of Language (0-10 marks), 
    Grammar and Mechanics (0-10 marks), 
    Originality and Creativity (0-10 marks), 
    Engagement of the Reader (0-10 marks), 
    Conclusion (0-10 marks)
    """

grade_ranges = "A (if marks 100-75), B (if marks 74-65), C (if marks 64-55), S (if marks 54-35), F (if marks 34-0)"

entered_essay = """
    Reading enriches our lives by exposing us to new ideas and perspectives. 
    It improves our vocabulary, enhances communication skills, and boosts cognitive functions. 
    By fostering empathy and expanding our knowledge, reading is a simple yet powerful tool for personal growth.
    """


# Calling the model
response = c.forward(entered_essay, evaluation_criteria, grade_ranges)

print("Grade = ", response['grade'])
print("Remark = ", response['remark'])
