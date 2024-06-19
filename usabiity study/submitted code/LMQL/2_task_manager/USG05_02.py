import lmql

# Define task contents
task_contents = [
    "Read a new book",
    "Go hiking with friends",
    "Complete the marketing report",
    "Prepare for the presentation",
    "Cook dinner for my family"
]

# Define Task class
class Task:
    def __init__(self, description, time=0, priority=0):
        self.description = description
        self.time = time
        self.priority = priority

    def __repr__(self):
        return f"Task(description={self.description}, time={self.time}, priority={self.priority})"

# Query template
query_template = '''
Given the following task: "{task}"
Estimate the completion time in minutes and the priority from 0 to 10.

Completion time: 
Priority: 
'''

# Function to get task details
def get_task_details(task_str):
    query = query_template.format(task=task_str)
    result = lmql.run(query)
    completion_time, priority = result['completion_time'], result['priority']
    return int(completion_time), int(priority)

# List to store task objects
tasks = []

# Process each task
for task_str in task_contents:
    completion_time, priority = get_task_details(task_str)
    task = Task(description=task_str, time=completion_time, priority=priority)
    tasks.append(task)

# Output the tasks
for task in tasks:
    print(task)
