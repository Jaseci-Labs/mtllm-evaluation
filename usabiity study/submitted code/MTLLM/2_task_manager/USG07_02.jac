task_contents = [
    "Read a new book",
    "Go hiking with friends",
    "Complete the marketing report",
    "Prepare for the presentation",
    "Cook dinner for my family"
]

def generate_task_objects(task_contents):
    import by_llm
    lm = by_llm.LLM()

    class Task:
        def _init_(self, description, time, priority):
            self.description = description
            self.time = time
            self.priority = priority

        def _repr_(self):
            return f"Task(description='{self.description}', time={self.time}, priority={self.priority})"

    tasks = []
    for task_description in task_contents:
        prompt = f"""
        Task: {task_description}

        Please provide the estimated time in minutes to complete this task and its priority on a scale of 0 to 10. Format your response as follows:
        Time: [time in minutes]
        Priority: [priority score]
        """
        
        response = lm.generate(prompt)
        output = response['generated_text']
        
        # Extract the time and priority from the response
        time_line = next(line for line in output.split('\n') if "Time:" in line)
        priority_line = next(line for line in output.split('\n') if "Priority:" in line)
        
        time = int(time_line.split(":")[1].strip())
        priority = int(priority_line.split(":")[1].strip())
        
        tasks.append(Task(description=task_description, time=time, priority=priority))
    
    return tasks
tasks = generate_task_objects(task_contents)

for task in tasks:
    print(task)
#task 2 LLM