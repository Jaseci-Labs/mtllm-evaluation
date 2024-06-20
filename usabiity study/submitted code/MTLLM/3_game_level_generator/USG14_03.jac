import:py from jaclang.core.llms, Anthropic;

glob llm = Anthropic(
            model_name = "claude-3-sonnet-20240229"
            );

obj 'Activity to-do'
Activity{
    has description: 'Thing that need to be complete': str,
        time: 'Estimated time to complete the activity': int,
        priority: 'Given priority rank for the activity from 1 to 10': int;
}

can 'Give a priority rank between to the given activity' 
make_priority(activity: 'Activity to give a priority number': str) -> 'Priority rank assigned to the given activity' int by llm();

can 'Estimate a time to complete the given activity'
set_time(activity: 'Activity to estimate a time to complete' : str) -> 'Estimated time to complete the activity': int by llm();

with entry{
    task_contents: list = [
        "Read a new book",
        "Go hiking with friends",
        "Complete the marketing report",
        "Prepare for the presentation",
        "Cook dinner for my family"
    ];
    output_list: list = [];

    for task in task_contents{
        priority_number = make_priority(task);
        estimated_time = set_time(task);
        task_description = task;

        task_todo: 'Activity object': Activity = Activity(description=task_description, time=estimated_time, priority=priority_number);

        output_list.append(task_todo);
    }
    print(output_list);
}