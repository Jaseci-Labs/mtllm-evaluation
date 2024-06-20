import:py from jaclang.core.llms, Anthropic;

glob llm = Anthropic(model_name="claude-3-sonnet-20240229");

def determine_priority(description):
    # Define keywords for each priority level
    high_priority_keywords = ['urgent', 'important', 'deadline']
    medium_priority_keywords = ['review', 'follow up']
    low_priority_keywords = ['research', 'compile']

    # Check if any keywords for high priority are present in the description
    for keyword in high_priority_keywords:
        if keyword in description.lower():
            return 10  # High priority

    # Check if any keywords for medium priority are present in the description
    for keyword in medium_priority_keywords:
        if keyword in description.lower():
            return 5  # Medium priority

    # Default to low priority if no specific keywords are found
    return 1  # Low priority

obj Task {
    has description: 'Description': str;
    has time: 'Time': int;
    has priority: 'Priority': int;

    can 'Get the estimated time for completion'
    get_time() -> 'Time': int by llm(incl_info=(self.description));

    can 'Get the priority of the task (0-10)'
    get_priority() -> 'Priority': int {
        return determine_priority(self.description);
    }
}

with entry {
    task_contents = [
        "Create presentation slides for the urgent meeting",
        "Review and finalize project proposal",
        "Follow up with client regarding project updates",
        "Research and compile data for quarterly report"
    ];

    tasks_list = {};
    for task_description in task_contents {
        new_task = Task(description=task_description, time=0, priority=0);  # Default values for time and priority
        time = new_task.get_time();
        priority = new_task.get_priority();
        tasks_list[task_description] = {"description": task_description, "time": time, "priority": priority};
    }

    # Print the list of Task objects
    for task in tasks_list.items() {
        print(task[0],": ",task[1]);
    }
}



