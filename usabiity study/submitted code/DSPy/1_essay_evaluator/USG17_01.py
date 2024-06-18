import dspy
from dspy.signatures.signature import signature_to_template

# Define the EssayRemark signature
class EssayRemark(dspy.Signature):
    """Evaluate an essay by the criteria given and give a remark about the text without repreating the text also give a grade from A,B,C,D,S,F"""
    essay = dspy.InputField()
    essay_remark = dspy.OutputField()

# Set up OpenAI model

turbo = dspy.OpenAI(model='gpt-3.5-turbo', max_tokens=1000) 

llm = dspy.OpenAI(model="gpt-4o")
dspy.settings.configure(lm=llm)

# Convert EssayRemark signature to template
essay_remark_as_template = signature_to_template(EssayRemark)

# Define ChainOfThought module
class CoT(dspy.Module):
    def __init__(self):
        super().__init__()
        self.prog = dspy.ChainOfThought(EssayRemark)
    
    def forward(self, essay):
        return self.prog(essay=essay)

# Instantiate CoT module
c = CoT()

# Get input essay from user
text = input("Enter your essay and the criteria : ")

# Generate essay remark and grade using ChainOfThought module
output = c.forward(text)

# Print the essay remark
print(output)
