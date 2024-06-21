import dspy

# Initialize the model
# phi3 = dspy.dspy.OllamaLocal(model="phi3:3.8b")

llm = dspy.OpenAI(model="gpt-4o")
dspy.settings.configure(lm=llm)

task_contents = [
    "Read a new book",
    "Go hiking with friends",
    "Complete the marketing report",
    "Prepare for the presentation",
    "Cook dinner for my family",
]


class Task(dspy.Signature):
    """provide one description for each task provided in task contents , estimated time(Estimated time in minutes for one task to finish the job), and priority(Estimated Priority for the provided Task_contents only (0-10)). do not include other tasks or subtasks out side from the given tasks .only include the taks in the task content list"""

    description: str = dspy.InputField()
    time: int = dspy.OutputField()
    priority: int = dspy.OutputField()


# List to store task objects
tasks = {}

with dspy.context(lm=llm):
    for task_content in task_contents:
        # Create task objects
        task = dspy.Predict(Task)(description=task_content)

        # Extract fields from the prediction result
        description = task_content
        time = getattr(task, "time", None)
        priority = getattr(task, "priority", None)

        tasks[task_content] = {"time": time, "priority": priority}


# Print out the tasks with their estimated time and priority
for task, details in tasks.items():
    print("Task: ", task)
    print(details["time"])
    print("Priority:", details["priority"])
    print("\n")
