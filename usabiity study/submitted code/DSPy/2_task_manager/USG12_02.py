import dspy

# List of tasks
task_list = [
    "Read a new book",
    "Go hiking with friends",
    "Complete the marketing report",
    "Prepare for the presentation",
    "Cook dinner for my family",
]


class Priority(dspy.Signature):
    """Assign priority based on general public opinion"""

    task_description = dspy.InputField()
    priority_level = dspy.OutputField()


class Duration(dspy.Signature):
    """Estimate time taken to complete the task"""

    task_description = dspy.InputField()
    estimated_time = dspy.OutputField()


# Configure the local model
ollama_model = dspy.OllamaLocal(model="phi3:3.8b")
dspy.settings.configure(lm=ollama_model)

llm = dspy.OpenAI(model="gpt-4o")
dspy.settings.configure(lm=llm)

# Criteria for evaluation
priority_criteria = "Categorize these into a number between 1-10 based on general public. 10 means least priority and 1 means high priority. No reasons"
time_criteria = "Estimate time in minutes taken to complete this task in general. Output only an integer number with no reasons"


def evaluate_priority(criteria, task_description):
    Priority._doc_ = criteria
    classifier = dspy.Predict(Priority)
    result = classifier(task_description=task_description)
    lines = result.priority_level.split("\n")
    for line in lines:
        if line.startswith("Grade:"):
            return int(line.split(": ")[1])


def estimate_time(criteria, task_description):
    Duration._doc_ = criteria
    classifier = dspy.Predict(Duration)
    result = classifier(task_description=task_description)
    return result.estimated_time


evaluation_results = []
for task in task_list:
    task_data = []

    estimated_time = estimate_time(time_criteria, task)
    priority_level = evaluate_priority(priority_criteria, task)

    task_data.append(task)
    task_data.append(priority_level)
    task_data.append(estimated_time)

    print(task_data)
    evaluation_results.append(task_data)
