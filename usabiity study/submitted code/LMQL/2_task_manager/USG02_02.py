import lmql

@lmql.query
def manage_tasks(task_list: list):
    '''lmql
    argmax
        task_objs = []
        for task in task_list:
            description = task
            priority = "Assign a priority rank (0-10) to the task: " + task
            time = "Estimate the time (in minutes) required to complete the task: " + task
            task_objs.append({"description": description, "priority": priority, "time": time})
        task_objs
    clause
    '''
    pass

task_contents = [
    "Read a new book",
    "Go hiking with friends",
    "Complete the marketing report",
    "Prepare for the presentation",
    "Cook dinner for my family"
]

task_list = manage_tasks(task_contents)
print(task_list)
