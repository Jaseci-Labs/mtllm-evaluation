task_contents=[
    "Read a new book",
    "Go hiking with friends",
    "Complete the marketing report",
    "Prepare for the presentation",
    "Cook dinner for my family"
]

class TaskObject(Task):
    description: str
    time: int
    priority: int

    def _init_(self, description):
        self.description=description
        super()._init_()
    def generate(self):
        f"""
For task: "{self.description}":
- Estimated time to complete the task (in minutes)
- Estimated priority (0-10)

Format: "time: [time], priority: [priority]"
""" 