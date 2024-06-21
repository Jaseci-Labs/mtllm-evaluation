import openai, dspy

openai.api_key = "openai-api-key"

llm = dspy.OpenAI(model="gpt-4o")
dspy.settings.configure(lm=llm)


def manage_tasks(task_list):
    task_objs = []
    for task in task_list:
        response_priority = openai.Completion.create(
            engine="text-davinci-003",
            prompt=f"Assign a priority rank (0-10) to the task: {task}",
            max_tokens=10,
        )
        response_time_estimate = openai.Completion.create(
            engine="text-davinci-003",
            prompt=f"Estimate the time (in minutes) required to complete the task: {task}",
            max_tokens=10,
        )
        task_obj = {
            "description": task,
            "priority": int(response_priority.choices[0].text.strip()),
            "time": int(response_time_estimate.choices[0].text.strip()),
        }
        task_objs.append(task_obj)
    return task_objs


task_contents = [
    "Read a new book",
    "Go hiking with friends",
    "Complete the marketing report",
    "Prepare for the presentation",
    "Cook dinner for my family",
]

task_list = manage_tasks(task_contents)
print(task_list)
