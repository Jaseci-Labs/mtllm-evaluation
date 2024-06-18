import:py random;

# Define the Task class
obj Task {
    has description: str;
    has time: int;
    has priority: int;
    
    can init(description: str, time: int, priority: int) {
        here.description = description;
        here.time = time;
        here.priority = priority;
    }
}

# Define the task_contents list
task_contents = [
    "Read a new book",
    "Go hiking with friends",
    "Complete the marketing report",
    "Prepare for the presentation",
    "Cook dinner for my family"
]

# Use the MTLLM framework to convert task descriptions into Task objects
obj TaskManager {
    has task_list: list[Task];
    
    can init {
        here.task_list = [];
        
        for task_description in task_contents {
            task = create_task(task_description);
            here.task_list.append(task);
        }
    }
    
    can create_task(description: str) -> Task {
        # Logic to assign priority rank and estimated time for completion
        # This can be based on certain criteria or rules
        
        #  let's assign random priority and time
        
        time = random.randint(30, 120)  # Random time between 30 to 120 minutes
        priority = random.randint(0, 10)  # Random priority between 0 to 10
        
        return Task(description, time, priority);
    }
}

# Creating a TaskManager instance
task_manager = TaskManager();

# Access the task_list
print("Task List:")
for task in task_manager.task_list {
    print(f"Description: {task.description}, Time: {task.time} minutes, Priority: {task.priority}")
}