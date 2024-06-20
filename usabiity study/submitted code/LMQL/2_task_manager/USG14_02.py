import lmql
import asyncio

class Activity:
    def __init__(self, description, time, priority):
        self.description = description
        self.time = time
        self.priority = priority

    def __repr__(self):
        return f"Activity(description='{self.description}', time={self.time}, priority={self.priority})"

@lmql.query
async def make_priority(activity: str):
    '''
    lmql
    "Give a priority rank between 1 to 10 to the given activity: {activity}"
    '''

@lmql.query
async def set_time(activity: str):
    '''
    lmql
    "Estimate the time to complete the given activity in hours: {activity}"
    '''

async def main():
    task_contents = [
        "Read a new book",
        "Go hiking with friends",
        "Complete the marketing report",
        "Prepare for the presentation",
        "Cook dinner for my family"
    ]
    
    output_list = []

    for task in task_contents:
        priority_number = await make_priority(task)
        estimated_time = await set_time(task)
        task_description = task

        task_todo = Activity(description=task_description, time=estimated_time, priority=priority_number)
        output_list.append(task_todo)
    
    print(output_list)

if __name__ == "__main__":
    asyncio.run(main())
