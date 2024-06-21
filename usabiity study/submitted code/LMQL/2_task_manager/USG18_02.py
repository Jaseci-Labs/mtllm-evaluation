import lmql

lmql_engine = lmql.Engine()


def determine_priority(description):
    # keywords for each priority level
    high_priority_keywords = ["urgent", "important", "deadline"]
    medium_priority_keywords = ["review", "follow up"]
    low_priority_keywords = ["research", "compile"]

    for keyword in high_priority_keywords:
        if keyword in description.lower():
            return "High"

    for keyword in medium_priority_keywords:
        if keyword in description.lower():
            return "Medium"

    return "Low"  # default


def add_task(description):
    priority = determine_priority(description)
    response = lmql_engine.query(
        f"""
    Analyze task description: '{description}'
    Determine estimated time based on priority: {priority}
    [TASK_DETAILS]
    """
    )
    task_details = response["TASK_DETAILS"]
    task_details["priority"] = priority
    return task_details


def main():
    # samples
    tasks = [
        "Create presentation slides for the urgent meeting",
        "Review and finalize project proposal",
        "Follow up with client regarding project updates",
        "Research and compile data for quarterly report",
    ]

    for task_description in tasks:
        task_details = add_task(task_description)
        print(f"Task added: {task_description}")
        print(f"Priority: {task_details['priority']}")
        print(f"Estimated Time: {task_details['estimated_time']}")
        print()


if __name__ == "_main_":
    main()
