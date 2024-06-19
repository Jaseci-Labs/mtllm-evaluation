import:py dspy ;
import:py from pydantic, BaseModel, Field ;

with entry {
    llm = dspy.OpenAI(model="gpt-4o");    
    dspy.settings.configure(lm=llm) ;
}

class Task : BaseModel : {
    with entry {
        description: str = Field(description="Content of the Job to be done");    
        time: int = Field(
            description="Estimated time in minutes for one to finish the job"
        );    
        priority: int = Field(
            description="Estimated Priority for the Task (0-10)"
        );
    }
}

"""Get Task."""
class GetTask : dspy.Signature : {
    with entry {
        info: str = dspy.InputField(desc="Task Information");    
        task: Task = dspy.OutputField();
    }
}

with entry {
    task_contents = [
        "Have some sleep",
        "Enjoy a better weekend with my girlfriend",
        "Work on Jaseci Project",
        "Teach EECS 281 Students",
        "Enjoy family time with my parents"
    ];    
    tasks = [];    
    for task_content in task_contents {
        task = dspy.TypedPredictor(GetTask)(info=task_content).task;    
        tasks.append(task) ;
    }
    
    print(tasks) ;
}

