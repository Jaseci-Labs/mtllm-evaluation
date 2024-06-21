from jaseci.jsorc.jsorc import JsOrc
from jaseci.jsorc.live_actions import jaseci_action, load_local_actions
from jaseci.utils.utils import JsObj


# Custom Action to estimate time and priority
@jaseci_action()
def estimate_time_and_priority(description: str) -> dict:
    """
    Estimate time and priority for a given task description.
    This is a placeholder function; replace with actual MTLLM model calls.

    Args:
    - description (str): The task description.

    Returns:
    - dict: A dictionary containing estimated time and priority.
    """
    # Example logic for time estimation
    time = len(description) * 10  # Example: Time based on description length
    priority = (
        len(description) % 10
    ) + 1  # Example: Priority based on description length modulo 10
    return {"time": time, "priority": priority}


# Load custom actions
load_local_actions(__file__)  # Ensures the current script's directory is used

# Jac code for the task manager
jac_code = """
walker TaskManager {
    has string description;  // Task description
    has int time;            // Estimated time to complete the task
    has int priority;        // Task priority (0-10)

    can init_with (string desc) {
        description = desc;  // Initialize with the given description
    }

    can estimate_time_and_priority {
        report('Estimating time and priority for: ' + description);
        dict result = estimate_time_and_priority(description);  // Call the custom action
        time = result.time;  // Set the estimated time
        priority = result.priority;  // Set the estimated priority
        report('Time: ' + time + ', Priority: ' + priority);
    }
}
"""

# Initialize Jaseci Object
js = JsObj()

# Load the Jac code
js.register_jac_code(jac_code)

# Example task list
task_contents = [
    "Read a new book",
    "Go hiking with friends",
    "Complete the marketing report",
    "Prepare for the presentation",
    "Cook dinner for my family",
]

# List to store task objects
tasks = []

# Process each task
for task_description in task_contents:
    # Initialize the TaskManager walker
    task_manager = js.create_walker(
        name="TaskManager", params={"desc": task_description}
    )

    # Execute the method to estimate time and priority
    task_manager.run(method="estimate_time_and_priority")

    # Collect task data
    task = {
        "description": task_manager.vars.description,
        "time": task_manager.vars.time,
        "priority": task_manager.vars.priority,
    }
    tasks.append(task)

# Print tasks
for task in tasks:
    print(task)
