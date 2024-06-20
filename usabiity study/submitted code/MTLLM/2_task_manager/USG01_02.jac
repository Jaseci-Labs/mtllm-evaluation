import:py from jaclang.core.llms, OpenAI;

glob llm = OpenAI(
    model_name = "gpt-4o"
);

obj 'Task'
Task {
    has description: 'Description of the task': str,
        time: 'Estimated time ': int = None,
        priority: 'Priority': int = None;

    can 
    taskTime(task: 'task': str) 
    -> 'Estimated time for the task': int by llm();

    can 
    taskPriority(task: 'task': str) 
    -> 'Priority of the task using a number between 1 and 10. 1 for the highest priority': int by llm();
}

walker TaskGenerator {
    has tasksInit: list[str],
        tasks: list[Task] = [];

    can create {
        for task1 in self.tasksInit {
            task = Task(description=task1);
            task.time = task.taskTime(task=task1);
            task.priority = task.taskPriority(task=task1);
            self.tasks.append(task);
        }
        
    }

    can outputTask {
        for task in self.tasks {
            print(task.description+" "+str(task.time)+" "+str(task.priority));
        }
    }
}

with entry {
    taskList = TaskGenerator(tasksInit=[
        "Read a new book",
        "Go hiking with friends",
        "Complete the marketing report",
        "Prepare for the presentation",
        "Cook dinner for my family"
    ]);

    print(taskList.create());
    print(taskList.outputTask());
}