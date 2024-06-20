import:py time;

import:py from jaclang.core.llms, OpenAI;

glob llm = OpenAI(
    model_name = "gpt-4o"
);


glob task_contents : 'List of Tasks to be done' : list = [
    "Read a book",
    "Go hiking with friends",
    "Complete the marketing report",
    "Do the heart surgery",
    "Make a party tonight to drink arake"
    "Prepare for the presentation",
    "Cook dinner for my family"
];

glob ranked_tasks = [];


obj 'Task'
Task {
    has description: 'Description about the task' : str,
        time: 'Estimated time in minutes for one to do the task' : int,
        priority: 'Estimated Priority for the Task (0-10)': int;
}


obj 'TaskList'
TaskList {
    has tasks: 'List of tasks' : list[Task];
}


with entry {
    
    task_list = TaskList(by llm(incl_info=(task_contents)));
    ranked_tasks=task_list.tasks;
    
    for i=0 to i<len(ranked_tasks) by i+=1 {
        print(ranked_tasks[i]);
    }
}