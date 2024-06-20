from transformers import pipeline

task_contents = [
    "Read a new book",
    "Go hiking with friends",
    "Complete the marketing report",
    "Prepare for the presentation",
    "Cook dinner for my family"
]

model_name = "gpt-4"  # Example model from OpenAI or other appropriate LLM
llm_pipeline = pipeline('text-generation', model=model_name)

class Task:
    def _init_(self, description, time, priority):
        self.description = description
        self.time = time
        self.priority = priority

    def _repr_(self):
        return f"Task(description='{self.description}', time={self.time}, priority={self.priority})"

def generate_task_attributes(task_description):
    prompt = f"""
    Task: {task_description}

    Please provide the estimated time in minutes to complete this task and its priority on a scale of 0 to 10. Format your response as follows:
    Time: [time in minutes]
    Priority: [priority score]
    """
    
    response = llm_pipeline(prompt, max_length=50, num_return_sequences=1)
    output = response[0]['generated_text']
    
    time_line = next(line for line in output.split('\n') if "Time:" in line)
    priority_line = next(line for line in output.split('\n') if "Priority:" in line)
    
    time = int(time_line.split(":")[1].strip())
    priority = int(priority_line.split(":")[1].strip())
    
    return Task(description=task_description, time=time, priority=priority)

tasks = [generate_task_attributes(task) for task in task_contents]

for task in tasks:
    print(task)
#task 2 DSPY