import dspy

# This is the configuration of Anthropic Claude-3 model. The code is included in the following google colab link.
# https://colab.research.google.com/drive/1xooazoy49vPspFrtNGKgbATCfpAJUji7?usp=sharing
# from model_config.anthropic import Claude


# claude_model = Claude(model="claude-3-sonnet-20240229")
# dspy.configure(lm=claude_model)

llm = dspy.OpenAI(model="gpt-4o")
dspy.settings.configure(lm=llm)


# Define the Task object
class Task():
    def __init__(self, description, time=0, priority=0):
        self.description = description
        self.time = time
        self.priority = priority

# Task Manager Template
class TaskManager(dspy.Signature):
    """Assign a given task a priority rank, and an estimated time for completion. Answer questions with short factoid answers."""
    current_task = dspy.InputField()
    all_tasks = dspy.InputField(format=list)

    completion_time = dspy.OutputField(desc="Estimated time in minutes for one to do the task. Answer only the time value.")
    priority = dspy.OutputField(desc="Estimated Priority for the Task number between 0 and 10. Answer only the number value.")

class COT(dspy.Module):
    def __init__(self):
        super().__init__()
        self.prog = dspy.ChainOfThought(TaskManager)

    def forward(self, task_str, all_tasks):
        try:
            return self.prog(current_task=task_str, all_tasks=all_tasks)
        except Exception as e:
            print(f"Error occurred: {e}")
            return {'completion_time': 'Unknown', 'priority': 'Unknown'}

c = COT()

# Define task contents
task_contents = [
    "Read a book",
    "Go hiking with friends",
    "Complete the marketing report",
    "Do the heart surgery",
    "Prepare for the presentation",
]

for current_task in task_contents:
    task = Task(description=current_task)
    response = c.forward(current_task, ','.join(task_contents))
    
    task.priority = response['priority']
    task.time = response['completion_time']

    # Print each response
    print(task.__dict__)