# Define the list of task descriptions
task_contents = [
    "Read a new book",
    "Go hiking with friends",
    "Complete the marketing report",
    "Prepare for the presentation",
    "Cook dinner for my family"
]

# Function to create task objects from task descriptions
def create_task_objects(task_list):
    task_objects = []
    for description in task_list:
        
        time_estimate = 60  # Placeholder for estimated time in minutes
        priority_estimate = 5  # Placeholder for estimated priority (0-10)

        # Create a task object dictionary with description, time, and priority
        task_object = {
            "description": description,
            "time": time_estimate,
            "priority": priority_estimate
        }

        # Append the task object to the list of task objects
        task_objects.append(task_object)

    return task_objects

# Create task objects using the function
task_objects = create_task_objects(task_contents)

# Print the list of task objects
for task in task_objects:
    print(f"Description: {task['description']}, Time: {task['time']} minutes, Priority: {task['priority']}")
