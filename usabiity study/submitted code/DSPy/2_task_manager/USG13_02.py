from dsp import LM
import requests
import dspy


# claude_model = Anthropic(model="claude-3-sonnet-20240229")
# dspy.configure(lm=claude_model)

llm = dspy.OpenAI(model="gpt-4o")
dspy.settings.configure(lm=llm)


class Task:
    def __init__(self, description, time=0, priority=0):
        self.description = description
        self.time = time
        self.priority = priority


class TaskManager(dspy.Signature):
    """Assign a given task a priority rank, and an estimated time for completion. Answer questions with short factoid answers."""

    current_task = dspy.InputField()
    all_tasks = dspy.InputField(format=list)

    completion_time = dspy.OutputField(
        desc="Estimated time in minutes for one to do the task. Answer questions with short factoid answers."
    )
    priority = dspy.OutputField(
        desc="Estimated Priority for the Task number between 0 and 10"
    )


class CoT(dspy.Module):
    def __init__(self):
        super().__init__()
        self.prog = dspy.ChainOfThought(TaskManager)

    def forward(self, task_str, all_tasks):
        return self.prog(current_task=task_str, all_tasks=all_tasks)


c = CoT()

task_contents = [
    "Read a book",
    "Complete the marketing report",
    "Do the heart surgery",
    "Make a party tonight to drink arake",
    "Prepare for the presentation",
    "Cook dinner for my family",
]

prioratized_tasks_list = []

for current_task in task_contents:
    task = Task(description=current_task)
    response = c.forward(current_task, task_contents)
    task.priority = response["priority"]
    task.time = response["completion_time"]
    prioratized_tasks_list.append(task.__dict__)

for task in prioratized_tasks_list:
    print(task)
