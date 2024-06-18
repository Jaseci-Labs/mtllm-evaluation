import:py from jaclang.core.llms, Ollama;

glob llm = Ollama(
    model_name = "phi3:3.8b"
);

obj 'Task'
Task {
    has description: 'Description of the task': str,
        time: 'Estimated time for completion in minutes': int = None,
        priority: 'Priority of the task (0-10)': int = None;

    can 'Estimate the time taken for completion of the task'
    Estimate(task: 'Task Description': str) 
    -> 'Estimated time': int by llm();

    can 'Set the priority of the task from 0 to 10'
    Prioritize(task: 'Task Description': str) 
    -> 'Priority of the task (0-10)': int by llm();
}

walker TaskGenerator {
    has task_contents: list[str],
        tasks: list[Task] = [];

    can gen_tasks {
        for task_description in self.task_contents {
            task = Task(description=task_description);
            task.time = task.Estimate(task=task_description);
            task.priority = task.Prioritize(task=task_description);
            self.tasks.append(task);
        }
        
    }

    can show_tasks {
        for task in self.tasks {
            print(f"Task(description='{task.description}', time={task.time}, priority={task.priority})");
        }
    }
}

with entry {
    task_list = TaskGenerator(task_contents=[
        "Read a new book",
        "Go hiking with friends",
        "Complete the marketing report",
        "Prepare for the presentation",
        "Cook dinner for my family"
    ]);

    print(task_list.gen_tasks());
    print(task_list.show_tasks());
}



