# Import the dspy library to use its functionalities
import dspy

# Define a Task class to represent each task with the required attributes
class Task:
    def __init__(self, description, time, priority):
        self.description = description  # Task description
        self.time = time  # Estimated time to complete the task in minutes
        self.priority = priority  # Priority of the task (0-10)

    def __repr__(self):
        return f"Task(description={self.description}, time={self.time}, priority={self.priority})"

# Function to generate task attributes using the language model
def generate_task_attributes(task_description):
    # Define the input prompt for the language model
    prompt = f"Given the task '{task_description}', estimate the time in minutes and priority (0-10)."

    # Generate the response using the language model
    response = llm.complete(prompt)

    # Extract the time and priority from the response
    try:
        lines = response.strip().split("\n")
        time = int(lines[0].split(":")[1].strip())  # Extract time from the response
        priority = int(lines[1].split(":")[1].strip())  # Extract priority from the response
    except Exception as e:
        print(f"Error parsing response: {e}")
        time = 60  # Default time if parsing fails
        priority = 5  # Default priority if parsing fails

    return time, priority  # Return the extracted time and priority

# # Configure DsPy with OpenAI GPT-3.5-turbo
# turbo = dspy.OpenAI(model="gpt-3.5-turbo")
# dspy.settings.configure(lm=turbo)


llm = dspy.OpenAI(model="gpt-4o")
dspy.settings.configure(lm=llm)

task_contents = [
    "Read a new book",
    "Go hiking with friends",
    "Complete the marketing report",
    "Prepare for the presentation",
    "Cook dinner for my family"
]

# Create an empty list to store task objects
tasks = []

# Generate task objects and add them to the list
for task_description in task_contents:
    time, priority = generate_task_attributes(task_description)  # Generate attributes for each task
    task = Task(description=task_description, time=time, priority=priority)  # Create a Task object
    tasks.append(task)  # Add the Task object to the list

# Print the tasks
for task in tasks:
    print(task)  # Print each task in the list
