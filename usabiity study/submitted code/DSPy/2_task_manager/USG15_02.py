import dspy

# ollama_model = dspy.OllamaLocal(
#     model="llama2",
#     model_type='text',
#     max_tokens=350,
#     temperature=0.0,
#     top_p=0.8,
#     frequency_penalty=1.17,
#     top_k=40
# )

# dspy.settings.configure(lm=ollama_model)

llm = dspy.OpenAI(model="gpt-4o")
dspy.settings.configure(lm=llm)


class Task:
    def __init__(self, description, time, priority):
        self.description = description
        self.time = time
        self.priority = priority

    def __str__(self):
        return f"Task(description='{self.description}', time='{self.time}', priority='{self.priority}')"


def generate_task_attributes(task_description):
    constraint = "In 3 words"
    time_prompt = f"{constraint} give the estimated time in minutes for completion of the task: '{task_description}'? Give the output without the reasoning or descriptions in the form Time estiamated is:"
    time_response = llm(time_prompt)
    time_str = time_response

    priority_prompt = f"{constraint} give the priority rank (0-10) for the task: '{task_description}'?"
    priority_response = llm(priority_prompt)
    priority_str = priority_response

    return time_str, priority_str


def create_task_list(task_contents):
    task_list = []
    for task_description in task_contents:
        try:
            time, priority = generate_task_attributes(task_description)
            task = Task(description=task_description, time=time, priority=priority)
            task_list.append(task)
        except ValueError as e:
            print(f"Error processing task '{task_description}': {e}")
    return task_list


def print_task_list(task_list):
    for task in task_list:
        print(f"Description: {task.description}")
        print(f"{task.time[0]}")
        print(f"{task.priority[0]}")
        print("----------------------")


"""task_contents = [
    'Read a new book',
    'Go hiking with friends',
    'Complete the marketing report',
    'Prepare for the presentation',
    'Cook dinner for my family'
]"""

task_contents = [
    "Drink water",
    "Have lunch",
    "Do school homework",
    "Go on a trip to the zoo",
]

task_list = create_task_list(task_contents)
print_task_list(task_list)
