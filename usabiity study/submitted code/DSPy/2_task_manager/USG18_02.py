import dspy

# phi3 = dspy.OllamaLocal(model="phi3")


llm = dspy.OpenAI(model="gpt-4o")
dspy.settings.configure(lm=llm)


def determine_priority(description):
    high_priority_keywords = ["urgent", "important", "deadline"]
    medium_priority_keywords = ["review", "follow up"]
    low_priority_keywords = ["research", "compile"]

    for keyword in high_priority_keywords:
        if keyword in description.lower():
            return "High"

    for keyword in medium_priority_keywords:
        if keyword in description.lower():
            return "Medium"

    return "Low"


class TaskManager(dspy.Signature):
    task: str = dspy.InputField()
    time: int = dspy.OutputField()


def add_task(description):
    priority = determine_priority(description)
    response = dspy.Predict(TaskManager)(task=description)
    time = response.time
    priority_value = 10 if priority == "High" else (5 if priority == "Medium" else 0)
    task_list[description] = {
        "description": description,
        "time": time,
        "priority": priority_value,
    }


task_list = {}


def main():
    # samples
    tasks = [
        "Create presentation slides for the urgent meeting",
        "Review and finalize project proposal",
        "Follow up with client regarding project updates",
        "Research and compile data for quarterly report",
    ]

    with dspy.context(lm=llm):
        for task_description in tasks:
            add_task(task_description)

    # Print the task list
    for task, task_info in task_list.items():
        print("Task:", task_info["description"])
        print("Time:", task_info["time"])
        print("Priority:", task_info["priority"])
        print()


if __name__ == "__main__":
    main()
