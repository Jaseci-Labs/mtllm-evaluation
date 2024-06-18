import math

object Task{
    has description str;
    has time int;
    has priority int;
}

object TaskManager{
    has task: list<Task>;
    can addTask(description:str) -> void{
        spawn{
            has description:description;
            f"Given task: {description}, estimated time to complete and priority rank (0-10).\n"
            f"Output format: time, priority\n"
            "[TIME], [PRIORITY]" where stops_at(TIME, ",") and stopes_at(PRIORITY, ".")

            let time = int(TIME);
            let priority = int(PRIORITY);

            Task(description=description, time=time, priority=priority);
        }
    }
    can populateTask(taskList:list<str>) -> void{
        for descrip in taskList{
            self.addTask(descrip);
        }
    }
}

with entry{
    let taskManager = TaskManager();
    taskManager.task=[];

    let taskContent = [
        "Read a new book",
        "Go hiking with friends",
        "Complete the marketing report",
        "Prepare for the presentation",
        "Cook dinner for my family"
    ];

    taskManager.populateTask(taskContent);

    for task in taskManager.task{
        print(f"Task:{task.description}, Time:{task.time} minutes, Priority:{task.priority}/10");
    }
}