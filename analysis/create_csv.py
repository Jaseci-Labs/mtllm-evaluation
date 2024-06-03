import os
import re
import csv

base_dir = ""  # Path to the directory to walk through
output_file = "token_usage.csv"


# Function to extract token counts from a line
def extract_tokens(line, pattern):
    match = re.search(pattern, line)
    if match:
        return {
            "completion_tokens": int(match.group("completion_tokens")),
            "prompt_tokens": int(match.group("prompt_tokens")),
            "total_tokens": int(match.group("total_tokens")),
        }
    return None


# Initialize the CSV file
with open(output_file, "w", newline="") as csvfile:
    fieldnames = [
        "directory",
        "type",
        "completion_tokens",
        "prompt_tokens",
        "total_tokens",
    ]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    # Walk through the directory structure
    for root, dirs, files in os.walk(base_dir):
        if "results.txt" in files:
            directory = os.path.relpath(root, base_dir)
            type = "MTLLM" if "jac" in directory else "dspy"

            with open(os.path.join(root, "results.txt"), "r") as f:
                for line in f:
                    if type == "MTLLM":
                        pattern = r"CompletionUsage\(completion_tokens=(?P<completion_tokens>\d+), prompt_tokens=(?P<prompt_tokens>\d+), total_tokens=(?P<total_tokens>\d+)\)"
                    else:  # dspy
                        pattern = r"'completion_tokens': (?P<completion_tokens>\d+), 'prompt_tokens': (?P<prompt_tokens>\d+), 'total_tokens': (?P<total_tokens>\d+)"

                    tokens = extract_tokens(line, pattern)
                    if tokens:
                        writer.writerow(
                            {**tokens, "directory": directory, "type": type}
                        )

print(f"CSV file '{output_file}' has been created.")
