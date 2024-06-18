import dspy
from dspy.signatures.signature import signature_to_template

class TaskAssigner(dspy.Signature):
    """Assign each task a description, priority rank(0-10), and an estimated time for completion based on the task"""
    taskList = dspy.InputField()
    edited_taskList = dspy.OutputField()


class Task:
    def __init__(self, description, priority, time):
        self.description = description
        self.priority = priority
        self.time = time



# Set up OpenAI model
# turbo = dspy.OpenAI(model='gpt-3.5-turbo', max_tokens=1000) 

llm = dspy.OpenAI(model="gpt-4o")
dspy.settings.configure(lm=llm)

task_assigner_as_template = signature_to_template(TaskAssigner)

# Define ChainOfThought module
class CoT(dspy.Module):
    def __init__(self):
        super().__init__()
        self.prog = dspy.ChainOfThought(TaskAssigner)
    
    def forward(self, taskList):
        return self.prog(taskList=taskList)

# Instantiate CoT module
c = CoT()

text = input("Enter your tasks : ")

output = c.forward(text)


print(output)
