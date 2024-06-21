import lmql

class Task:
    def __init__(self, description: str, time: int, priority: int):
        self.description = description
        self.time = time
        self.priority = priority


@lmql.query
def GetTask(task_info: str) -> Task:
    '''lmql
    "{task_info}.\n"
    "Structured: [TASK_DATA]\n" where type(TASK_DATA) is Task
    return TASK_DATA
    '''

task_contents = [
    "Have some sleep",
    "Enjoy a better weekend with my girlfriend",
    "Work on Jaseci Project",
    "Teach EECS 281 Students",
    "Enjoy family time with my parents",
]
tasks = []
for task_content in task_contents:
    task = GetTask(task_content)
    tasks.append(task)

print(tasks)


'''
    same error as Personality Finder
    
  File "/home/acer/miniconda3/lib/python3.12/site-packages/lmql/lib/types.py", line 24, in type_schema_description
    s = type_schema(t)
        ^^^^^^^^^^^^^^
  File "/home/acer/miniconda3/lib/python3.12/site-packages/lmql/lib/types.py", line 21, in type_schema
    assert False, "not a supported type " + str(t)
AssertionError: not a supported type <class '__main__.Task'>
'''