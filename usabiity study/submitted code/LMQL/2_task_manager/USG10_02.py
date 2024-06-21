import lmql

# Initialize LMQL engine
lmql_engine = lmql.Engine()


# Function to determine estimated time based on task description
def estimatedTime(description):
    # Use LMQL to analyze task description and estimate time
    response = lmql_engine.query(
        f"Analyse the task and find the estimated completion time '{description}': [ESTIMATED_TIME]"
    )
    estimated_time = response["ESTIMATED_TIME"]
    return estimated_time


# Function to determine priority level based on task description
def analyzePriority(description):
    # Use LMQL to analyze task description and determine priority level
    response = lmql_engine.query(
        f"Analyse the given task and assess the priority level '{description}': [PRIORITY]"
    )
    priority_level = response["PRIORITY"]
    return priority_level


# Main function to convert task list to task objects with filled out fields
def main():
    # Sample task descriptions
    task_descriptions = [
        "Read a new book",
        "Go hiking with friends",
        "Complete the marketing report",
        "Prepare for the presentation",
        "Cook dinner for my family",
    ]

    # List to store task objects
    tasks = []

    # Process each task description
    for description in task_descriptions:
        estimated_time = estimatedTime(description)
        priority_level = analyzePriority(description)
        task = {
            "description": description,
            "estimated_time": estimated_time,
            "priority_level": priority_level,
        }
        tasks.append(task)

    return tasks


if _name_ == "_main_":
    tasks = main()
    print("List of tasks:")
    for task in tasks:
        print(task)
