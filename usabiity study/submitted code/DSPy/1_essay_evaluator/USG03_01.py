import dspy

# Setup Ollama environment
ollama_mistral = dspy.OllamaLocal(model="phi3:3.8b")
dspy.settings.configure(lm=ollama_mistral)

llm = dspy.OpenAI(model="gpt-4o")
dspy.settings.configure(lm=llm)


class taskproritizer(dspy.Signature):
    """prioritize the list of tasks among 1 to 10 and estimate the time of completion"""

    task_list = dspy.InputField()
    tasks = dspy.OutputField()


task_list = [
    "Read a new book",
    "Go hiking with friends",
    "Complete the marketing report",
    "Prepare for the presentation",
    "Cook dinner for my family",
]
classify = dspy.Predict(taskproritizer)
classify(task_list=task_list)
