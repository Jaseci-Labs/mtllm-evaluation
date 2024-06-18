import:py from jaclang.core.llms, Ollama;

glob llm = Ollama(model_name="llama2:latest");

obj Task {
    has description: str,
    time: int,
    priority: int;

    can init(description: str) {
        self.description = description;
    }

    can 'Give single integer output of generated time estimate for completion of the task. Do not include explanaitions or additional text'
    generate_time(description: 'Description': str) -> 'Time': int by llm(method='Reason',incl_info=(self.description));

    can 'Give single integer output of generated a priority rank (0-10) for the task. Do not include reasoning or additional text'
    generate_priority(description: 'Description': str) -> 'Priority': int by llm(method='Reason', incl_info=(self.description));

    can initialize_task(task_description: str) -> void {
        self.time = self.generate_time(task_description);
        self.priority = self.generate_priority(task_description);
    }
}

with entry {
    task_contents = [
        'Read a new book',
        'Go hiking with friends',
        'Complete the marketing report',
        'Prepare for the presentation',
        'Cook dinner for my family'
    ];

    for task_description in task_contents {
        task = Task(description=task_description);
        task.initialize_task(task_description);
        print("Task: ", task.description);
        print("Time estimate: ", task.time);
        print("Priority rank: ", task.priority);
        print("-------------------------------");
    }

}
