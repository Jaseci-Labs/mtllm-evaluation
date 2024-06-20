import dspy
from dspy import ChainOfThought

class TaskSignature(dspy.Signature):
    description = dspy.InputField(desc="Task description")
    time = dspy.OutputField(desc="Estimated time in minutes")
    priority = dspy.OutputField(desc="Priority rank (0-10)")

class TaskManager(dspy.Program):
    def __init__(self):
        super().__init__()
        self.signature = TaskSignature()
        self.chain = ChainOfThought(self.signature)

    def __call__(self, task_list):
        tasks = []
        for task in task_list:
            task_obj = self.chain(description=task)
            tasks.append(task_obj)
        return tasks

task_contents = [
    "Read a new book",
    "Go hiking with friends",
    "Complete the marketing report",
    "Prepare for the presentation",
    "Cook dinner for my family"
]

task_manager = TaskManager()

for task in tasks:
    print(f"Description: {task.description}, Time: {task.time}, Priority: {task.priority}")
