from lmql import LMQL

# Initialize LMQL model
lmql_model = LMQL()

# Example task description
task_description = "Read a new book"

# Query LMQL to get estimated time and priority
query = f"Provide estimated time and priority for the task: {task_description}"
response = lmql_model.query(query)

# Extract time and priority from LMQL response
time_estimate = response.get("estimated_time", None)
priority_estimate = response.get("priority", None)

# Print the estimated time and priority
print("Estimated Time:", time_estimate)
print("Priority:", priority_estimate)
