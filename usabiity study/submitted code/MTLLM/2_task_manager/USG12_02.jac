import:py from jaclang.core.llms, Ollama;

glob llm_model = Ollama(
    model_name = "phi3:3.8b"
);

obj 'Task'
Task {
    has description: 'Description of the task': str,
        time: 'Estimated time for completion in minutes': int = None,
        priority: 'Priority of the task (0-10)': int = None;

    can 'Estimate the time taken for completion of the task'
    Estimate(task_info: 'Task Description': str) 
    -> 'Estimated time': int by llm_model();

    can 'Set the priority of the task from 0 to 10'
    Prioritize(task_info: 'Task Description': str) 
    -> 'Priority of the task (0-10)': int by llm_model();
}

walker TaskManager {
    has task_descriptions: list[str],
        tasks: list[Task] = [];

    can generate_tasks {
        for task_info in self.task_descriptions {
            task = Task(description=task_info);
            task.time = task.Estimate(task_info=task_info);
            task.priority = task.Prioritize(task_info=task_info);
            self.tasks.append(task);
        }
    }

    can display_tasks {
        for task in self.tasks {
            print(f"Task(description='{task.description}', time={task.time}, priority={task.priority})");
        }
    }
}

with entry {
    task_manager = TaskManager(task_descriptions=[
        "Read a new book",
        "Go hiking with friends",
        "Complete the marketing report",
        "Prepare for the presentation",
        "Cook dinner for my family"
    ]);

    print(task_manager.generate_tasks());
    print(task_manager.display_tasks());
}
