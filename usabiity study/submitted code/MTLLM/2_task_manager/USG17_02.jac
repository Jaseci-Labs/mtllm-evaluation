
import:py from jaclang.core.llms, Anthropic;


glob llm = Anthropic(model_name="claude-3-sonnet-20240229");


obj Task{
    has description:'Description about the task':str,
        time:'Estimated time in minutes from one to finsh the job':str,
        priority:'Estimated priority for the task (0-10)':int;
}


with entry{
    task_contents:'tasks list': list[str] = ["Go to hospital", "prepare for the tomorrow presentation", "Go hiking with friends", "Complete the marketing report","Prepare for today evening exam"];

    task_object = Task(by llm(incl_info = (task_contents)));
    for tasks in task_object{
    print(tasks);
    }
}

