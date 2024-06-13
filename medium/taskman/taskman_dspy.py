import dspy
from pydantic import BaseModel, Field

llm = dspy.OpenAI(model="gpt-4o")
dspy.settings.configure(lm=llm)


class Task(BaseModel):
    description: str = Field(description='Content of the Job to be done')
    time: int = Field(description='Estimated time in minutes for one to finish the job')
    priority: int = Field(description='Estimated Priority for the Task (0-10)')

class GetTask(dspy.Signature):
    """Get Task."""

    info: str = dspy.InputField(desc="Task Information")
    task: Task = dspy.OutputField()

task_contents = [
    "Complete the Medium Article",
    "Prepare for the upcoming Exam",
    "Finish the pending Project",
    "Clean the House",
    "Cook the Dinner",
]
tasks = []
for task_content in task_contents:
    task = dspy.TypedPredictor(GetTask)(info=task_content).task
    tasks.append(task)
print(tasks)