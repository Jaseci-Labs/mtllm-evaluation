import lmql

# llm = lmql.model("llama.cpp:/home/gayanukaa/llm-test/lmql-test/llama-2-7b.Q4_K_M.gguf", tokenizer="jodiambra/llama-2-7b-finetuned-python-qa_tokenizer", n_ctx=2048)
llm = lmql.model("openai/gpt-3.5-turbo-instruct")


class Task:
    def __init__(self, description, time, priority):
        self.description = description
        self.time = time
        self.priority = priority

    def __str__(self):
        return f"Task(description='{self.description}', time='{self.time}', priority='{self.priority}')"


@lmql.query(model=llm, lang="en")
def generate_time(description):
    """lmql
    "Q: Give the estimated time in minutes for completion of the task: '{description}'?\\n"
    "A: Time estimated is: [TIME]" where (len(TOKENS(TIME)) < 15) and STOPS_AT(TIME, '\\n')
    """


@lmql.query(model=llm, lang="en")
def generate_priority(description):
    """lmql
    "Q: Give the priority rank from (0 - 10) for the task: '{description}'?\\n"
    "A: Priority rank is: [PRIORITY]" where (len(TOKENS(PRIORITY)) < 10) and STOPS_AT(PRIORITY, '\\n')
    """


def generate_task_attributes(task_description):
    time_response = generate_time(task_description)
    time_str = time_response.variables["TIME"]

    priority_response = generate_priority(task_description)
    priority_str = priority_response.variables["PRIORITY"]

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
        print(f"Time: {task.time}")
        print(f"Priority: {task.priority}")
        print("----------------------")


task_contents = [
    "Read a new book",
    "Go hiking with friends",
    "Complete the marketing report",
    "Prepare for the presentation",
    "Cook dinner for my family",
]

# Create and print the task list
task_list = create_task_list(task_contents)
print_task_list(task_list)
