import:py from jaclang.core.llms, OpenAI;

glob llm = OpenAI(model_name="gpt-4o");

obj Task {
    has description: 'description about the task to be done': str;
    has time: 'Estimated time to finish the task': int,
    has priority: 'Estimated priority level of the task (0-10)': int;
}

with entry {
    task_contents = [
    "Read a new book",
    "Go hiking with friends",
    "Complete the marketing report",
    "Prepare for the presentation",
    "Cook dinner for my family"
    ];
    tasks = [];
    for task_content in task_contents {
    description = task_content;
    time = llm(method="Reason", input=f"Estimate the time to finish the task: {task_content}");
    priority = llm(method="Reason", input=f"Estimate the priority (0-10) for the task: {task_content}");
    
    task_info = Task(description=description, time=int(time), priority=int(priority));
    tasks.append(task_info);
}

    print(tasks);
}