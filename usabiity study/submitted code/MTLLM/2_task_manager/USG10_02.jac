import:py from jaclang.core.llms, OpenAI;

glob llm = OpenAI(
    model_name = "gpt-4o"
);

obj Task {
    has description: 'Description': str;
    has time: 'Time': int;
    has priority: 'Priority': int;

    can 'Generate description for the task.'
    get_description() -> 'Description': str by llm(incl_info=(self.description));
    
    can 'Generate  estimated time for completion of the task'
    assign_time() -> 'Time': int by llm(incl_info=(self.description));

    can 'Generate the priority of the task (0-10)'
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

    task_list = {};
    
    for task_content in task_contents {
        task = Task(description="", time=0, priority=0);
        description=task.get_description();
        time = task.assign_time();
        priority = task.get_priority();
        task_list[task_content] = {"description": description, "time": time, "priority": priority};


    }

    for task in task_list.items() {
        print(task[0],": ",task[1]);

    }

    
}

