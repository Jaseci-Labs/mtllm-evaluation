from mtllm import MTLLM

# Initialize MTLLM model
mtllm_model = MTLLM()

# Example task description
task_description = "Read a new book"

# Query MTLLM to get estimated time and priority
time_estimate, priority_estimate = mtllm_model.estimate(task_description)

# Print the estimated time and priority
print("Estimated Time:", time_estimate)
print("Priority:", priority_estimate)
