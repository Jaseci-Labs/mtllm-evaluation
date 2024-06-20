import:py from jaclang.core.llms, OpenAI;

glob llm = OpenAI(
    model_name = "gpt-4o"
);

obj Task {
    has description: 'Description': str;
    has time: 'Time': int;
    has priority: 'Priority': int;

    can 'Get the estimated time for completion'
    get_time() -> 'Time': int by llm(incl_info=(self.description));

    can 'Get the priority of the task (0-10)'
    get_priority() -> 'Priority': int by llm(incl_info=(self.description));
}

with entry {
    task_contents = [
        "Read a new book",
        "Go hiking with friends",
        "Complete the marketing report",
        "Prepare for the presentation",
        "Cook dinner for my family"
    ];

    tasks_list = {};
    for task_description in task_contents {
        new_task = Task(description=task_description, time=0, priority=0);  # You need to provide default values for time and priority
        time = new_task.get_time();
        priority = new_task.get_priority();
        tasks_list[task_description] = {"description": task_description, "time": time, "priority": priority};
    }

    # Print the list of Task objects
    for task in tasks_list.items() {
        print(task[0],": ",task[1]);
        
    }
}
