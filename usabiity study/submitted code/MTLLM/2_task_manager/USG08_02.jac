import:py from jaclang.core.llms, OpenAI;

glob llm = OpenAI(
    model_name = "gpt-4o"
);

obj Task {
    has description: 'Description': str;
    has time: 'Time': int;
    has priority: 'Priority': int;
}

obj TaskNode {
    has task: 'Task': Task;
    has next: 'Next': TaskNode;
}

with entry {
    task_contents = [
        "Read a new book",
        "Go hiking with friends",
        "Complete the marketing report",
        "Prepare for the presentation",
        "Cook dinner for my family"
    ];

    head = TaskNode(task=Task(description="", time=0, priority=0), next=None);
    current_node = head;
    
    for task_description in task_contents {
        task = Task(description=task_description, time=0, priority=0);
        new_node = TaskNode(task=task, next=None);
        current_node.next = new_node;
        current_node = new_node;
    }

    current_node = head.next;
    while current_node is not None {
        prompt = "Task: " + current_node.task.description + "\n";
        response = llm(prompt);
        current_node.task.time = response.time;
        current_node.task.priority = response.priority;
        current_node = current_node.next;
    }

    current_node = head.next;
    print("Task List:");
    while current_node is not None {
        print("- Description:", current_node.task.description);
        print("  Time:", current_node.task.time, "minutes");
        print("  Priority:", current_node.task.priority);
        current_node = current_node.next;
    }
}
