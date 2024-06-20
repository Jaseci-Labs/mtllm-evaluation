import lmql


# Function to determine priority and estimated time based on task description
def estimated_time(description):
    # Use LMQL to analyze task description and determine priority and estimated time
    time = lmql.F(
        "Analyse the task and give the estimated time to do the task in minutes {task}: [TIME]"
    )

    return time


def priority_level(description):
    # Use LMQL to analyze task description and determine priority and estimated time
    priority = lmql.F(
        "Analyse the task and give the priority level between 0 to 10 {task}: [PRIORITY]"
    )

    return priority


# Main function to convert task list to task objects with filled out fields
def main():
    # Example task descriptions
    task_contents = [
        "Read a new book",
        "Go hiking with friends",
        "Complete the marketing report",
        "Prepare for the presentation",
        "Cook dinner for my family",
    ]

    # List to store task objects
    task_list = []

    # Process each task description
    for task_description in task_contents:
        time = estimated_time(task_description)
        priority = priority_level(task_description)
        task_object = {
            "description": task_description,
            "time": time["estimated_time"],
            "priority": priority["priority"],
        }
        task_list.append(task_object)

    return task_list


if __name__ == "__main__":
    tasks = main()
    print("Task List:")
    for task in tasks:
        print(task)
