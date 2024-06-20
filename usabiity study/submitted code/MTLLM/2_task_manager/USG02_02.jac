import:py from jaclang.core.llms, OpenAI;
glob llm = OpenAI('gpt-4o');

obj task_manager {
    has tasks;

    can manage_tasks {
        report {
            task_objs = []
            for task in tasks:
                task_obj = {
                    description: task,
                    priority: llm.prompt("Assign a priority rank (0-10) to the task: " + task),
                    time: llm.prompt("Estimate the time (in minutes) required to complete the task: " + task)
                }
                task_objs.append(task_obj)
            }
            task_objs
        }
    }
}

with entry {
    spawn here > task_manager {
        tasks: [
            "Read a new book",
            "Go hiking with friends",
            "Complete the marketing report",
            "Prepare for the presentation",
            "Cook dinner for my family"
        ]
    };
    take > task_manager.manage_tasks;
    print(take)
}
