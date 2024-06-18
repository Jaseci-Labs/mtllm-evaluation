import:py from jaclang.core.llms, Anthropic;

glob llm = Anthropic(model_name="claude-3-sonnet-20240229");

obj 'Task object with all details.'
Task {
    has description: 'same as the task': str,
        time: 'Estimated time in minutes for one to finish the task': int,
        priority: 'estimated priority for the task as an integer between 1 to 10': int;
}


with entry {
    todo_list = ["Read a new book",
                        "Go hiking with friends",
                        "Complete the marketing report",
                        "Prepare for the presentation",
                        "Cook dinner for my family"
                        ];
    task_list=[];
    for task in todo_list {
        # task: 'task': str = "Read a newbook.";
        task = Task(by llm(incl_info=(task)));
        task_list.append(task);
        

    }
    print(*task_list, sep='\n');
}

