import lmql


# Define the LMQL query for task prioritization and time estimation
@lmql.query
def task_query(task_description: str, all_tasks: list):
    """
    # Task Manager Prompt
    Assign a given task a priority rank, and an estimated time for completion.
    Answer questions with short factoid answers.

    Task Description: {task_description}
    All Tasks: {all_tasks}

    Task Priority:
    Estimated Time for Completion:
    """
    priority = F("Task Priority: ")
    completion_time = F("Estimated Time for Completion: ")
    return priority, completion_time


# List of tasks
task_contents = [
    "Read a book",
    "Complete the marketing report",
    "Do the heart surgery",
    "Make a party tonight to drink arake",
    "Prepare for the presentation",
    "Cook dinner for my family",
]

prioritized_tasks_list = []

# Query the LM for each task
for current_task in task_contents:
    response = task_query(task_description=current_task, all_tasks=task_contents)
    task = {
        "description": current_task,
        "priority": response.priority,
        "time": response.completion_time,
    }
    prioritized_tasks_list.append(task)

# Print the tasks with priorities and estimated times
for task in prioritized_tasks_list:
    print(task)
