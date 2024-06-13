import:py from jaclang.core.llms, OpenAI, Ollama;

glob llm = OpenAI(model_name="gpt-3.5-turbo");

obj 'A work to be done in the future'
Task {
    has description: 'Content of the Job to be done': str;
    has time: 'Estimated time in minutes for one to finish the job': int,
        priority: 'Estimated Priority for the Task (0-10)': int;
}

with entry {
    task_contents = [
        "Complete the Medium Article",
        "Prepare for the upcoming Exam",
        "Finish the pending Project",
        "Clean the House",
        "Cook the Dinner"
    ];
    tasks = [];
    for task_content in task_contents {
        task_info = Task(description = task_content by llm(method="Reason"));
        tasks.append(task_info);
    }
    print(tasks);
}