import pandas as pd
from prettytable import PrettyTable

# Read the CSV data
data = pd.read_csv("token_usage.csv")

# Split the directory column into task and framework
data[["task", "framework"]] = data["directory"].str.split("/", expand=True)

# Group by task and framework, then calculate sum of tokens
grouped = data.groupby(["task", "type"]).agg(
    {"completion_tokens": "sum", "prompt_tokens": "sum", "total_tokens": "sum"}
)

# Reset index for easier access
grouped.reset_index(inplace=True)

# Create a PrettyTable
table = PrettyTable()
table.field_names = ["Task", "Metric", "DSPy", "MTLLM"]

# List of tasks and metrics
tasks = sorted(data["task"].unique())
metrics = ["completion_tokens", "prompt_tokens", "total_tokens"]

# Fill in the table
for task in tasks:
    for metric in metrics:
        dspy_data = grouped[(grouped["task"] == task) & (grouped["type"] == "dspy")]
        mtllm_data = grouped[(grouped["task"] == task) & (grouped["type"] == "MTLLM")]

        if not dspy_data.empty and not mtllm_data.empty:
            dspy_sum = dspy_data[metric].values[0]
            mtllm_sum = mtllm_data[metric].values[0]

            table.add_row(
                [
                    task,
                    metric.replace("_", " ").title(),
                    f"{dspy_sum:.0f}",
                    f"{mtllm_sum:.0f}",
                ]
            )

        elif not dspy_data.empty:
            dspy_sum = dspy_data[metric].values[0]
            table.add_row(
                [task, metric.replace("_", " ").title(), f"{dspy_sum:.0f}", "N/A"]
            )

        elif not mtllm_data.empty:
            mtllm_sum = mtllm_data[metric].values[0]
            table.add_row(
                [task, metric.replace("_", " ").title(), "N/A", f"{mtllm_sum:.0f}"]
            )

# Set table styles
table.align = "r"
table.align["Task"] = "l"
table.align["Metric"] = "l"

# Add a summary row for total tokens across all tasks
total_dspy = data[data["type"] == "dspy"]["total_tokens"].sum()
total_mtllm = data[data["type"] == "MTLLM"]["total_tokens"].sum()

# Print the table
print(table)
from PIL import Image, ImageDraw, ImageFont
from prettytable import PrettyTable



im = Image.new("RGB", (650, 750), "white")
draw = ImageDraw.Draw(im)
font = ImageFont.truetype("FreeMono.ttf", 15)
draw.text((10, 10), str(table), font=font, fill="black")



im.show()
im.save("table.png")