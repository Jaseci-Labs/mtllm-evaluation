import dspy

# phi3 = dspy.OllamaLocal(model="phi3")

llm = dspy.OpenAI(model="gpt-4o")
dspy.settings.configure(lm=llm)

tasks = [
    "Read a new book",
    "Go hiking with friends",
    "Complete the marketing report",
    "Prepare for the presentation",
    "Cook dinner for my family",
]


class TaskManager(dspy.Signature):
    "Time should indicate in minutes and priority should be a number between 0 and 10"
    task: str = dspy.InputField()
    time: int = dspy.OutputField()
    priority: int = dspy.OutputField(
        desc="This should be an integer between 0-10 where 10 is the maximum priority"
    )


task_list = {}


with dspy.context(lm=llm):
    for task in tasks:
        time = dspy.Predict(TaskManager)(task=task).time
        priority = dspy.Predict(TaskManager)(task=task).priority
        task_list[task] = {"description": task, "time": time, "priority": priority}

# Print the task list
for task, task_info in task_list.items():
    print("Task:", task_info["description"])
    print("Time:", task_info["time"])
    print("Priority:", task_info["priority"])
