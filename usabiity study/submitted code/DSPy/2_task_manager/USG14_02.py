import dspy

# from google.colab import userdata


class Activity:
    def __init__(self, description, time, priority):
        self.description = description
        self.time = time
        self.priority = priority

    def __repr__(self):
        return f"Activity(description='{self.description}', time={self.time}, priority={self.priority})"


class MakePriority(dspy.Signature):
    activity = dspy.InputField()
    priority_rank = dspy.OutputField()


class SetTime(dspy.Signature):
    activity = dspy.InputField()
    estimated_time = dspy.OutputField()


# OPENAI_API_KEY = userdata.get('OPENAI_API_KEY')

# turbo = dspy.OpenAI(model='gpt-3.5-turbo', max_tokens=1000, api_key=OPENAI_API_KEY)
# dspy.settings.configure(lm=turbo)

llm = dspy.OpenAI(model="gpt-4o")
dspy.settings.configure(lm=llm)

make_priority_template = dspy.signatures.signature_to_template(MakePriority)
set_time_template = dspy.signatures.signature_to_template(SetTime)


class TaskProcessor(dspy.Module):
    def __init__(self):
        super().__init__()
        self.priority_prog = dspy.ChainOfThought(MakePriority)
        self.time_prog = dspy.ChainOfThought(SetTime)

    def evaluate_task(self, task):
        priority = self.priority_prog(activity=task)
        time = self.time_prog(activity=task)
        return priority, time


task_processor = TaskProcessor()

if __name__ == "__main__":
    task_contents = [
        "Read a new book",
        "Go hiking with friends",
        "Complete the marketing report",
        "Prepare for the presentation",
        "Cook dinner for my family",
    ]

    output_list = []

    for task in task_contents:
        priority_number, estimated_time = task_processor.evaluate_task(task)
        task_description = task

        task_todo = Activity(
            description=task_description, time=estimated_time, priority=priority_number
        )
        output_list.append(task_todo)

    print(output_list)
