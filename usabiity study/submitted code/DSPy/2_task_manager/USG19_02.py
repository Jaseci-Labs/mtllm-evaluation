import dspy


class TaskManagerSignature(dspy.Signature):
    """Task management signature."""

    task = dspy.InputField(desc="Task content")
    priority = dspy.OutputField(desc="Priority rank")
    time_estimate = dspy.OutputField(desc="Estimated time for completion")


class TaskManager(dspy.Module):
    def __init__(self):
        super().__init__()

    def prioritize_task(self, task):
        # Placeholder logic for task prioritization
        return 1  # For demonstration, always returns priority 1

    def estimate_time(self, task):
        # Placeholder logic for time estimation
        return "2 hours"  # For demonstration, always returns 2 hours

    def forward(self, task):
        priority = self.prioritize_task(task)
        time_estimate = self.estimate_time(task)
        return dspy.Prediction(priority=priority, time_estimate=time_estimate)


task_contents = [
    "Read a new book",
    "Go hiking with friends",
    "Complete the marketing report",
    "Prepare for the presentation",
    "Cook dinner for my family",
]

task_manager = TaskManager()

for task_content in task_contents:
    prediction = task_manager(task=task_content)
    print(f"Task: {task_content}")
    print(f"Priority: {prediction.priority}")
    print(f"Time Estimate: {prediction.time_estimate}\n")
