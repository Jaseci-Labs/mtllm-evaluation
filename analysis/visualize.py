"""Visualize Completion token usage comparision. """

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("analysis/token_usage.csv")

# Group by 'directory' and 'type' and calculate the sum of completion tokens
completion_tokens_sum = (
    df.groupby(["directory", "type"])["completion_tokens"].sum().unstack()
)

ax = completion_tokens_sum.plot(
    kind="bar", figsize=(14, 8), color=["skyblue", "salmon"]
)

plt.title("Sum of Completion Tokens by Task and Type", fontsize=16)
plt.xlabel("Task", fontsize=14)
plt.ylabel("Sum of Completion Tokens", fontsize=14)

ax.set_xticklabels(completion_tokens_sum.index, rotation=45, ha="right")

for container in ax.containers:
    ax.bar_label(container, label_type="edge", fontsize=10)

plt.legend(title="Type", title_fontsize="13", fontsize="11")

plt.tight_layout()
plt.show()


# """To compare total token usage between 'jac' and 'dspy' for
#      each task, we can create a grouped bar chart."""

# import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sns

# df = pd.read_csv("token_usage.csv")

# df["task"] = df["directory"].apply(lambda x: x.split("/")[0])

# # Calculate total token usage by task and type
# total_by_task_type = (
#     df.groupby(["task", "type"])
#     .agg({"completion_tokens": "sum", "prompt_tokens": "sum", "total_tokens": "sum"})
#     .reset_index()
# )

# total_by_task = (
#     df.groupby("task")
#     .agg({"total_tokens": "sum"})
#     .sort_values("total_tokens", ascending=False)
# )

# ordered_tasks = total_by_task.index.tolist()

# plt.figure(figsize=(16, 8))
# bar_width = 0.4
# index = range(len(ordered_tasks))

# # Plot 'jac' and 'dspy' side by side for each task
# for i, task in enumerate(ordered_tasks):
#     jac_data = total_by_task_type[
#         (total_by_task_type["task"] == task) & (total_by_task_type["type"] == "jac")
#     ]
#     dspy_data = total_by_task_type[
#         (total_by_task_type["task"] == task) & (total_by_task_type["type"] == "dspy")
#     ]

#     # 'jac' bars
#     if not jac_data.empty:
#         plt.bar(
#             i - bar_width / 2,
#             jac_data["completion_tokens"],
#             bar_width,
#             label="jac (Completion)" if i == 0 else None,
#             alpha=0.8,
#             color="skyblue",
#         )
#         plt.bar(
#             i - bar_width / 2,
#             jac_data["prompt_tokens"],
#             bar_width,
#             bottom=jac_data["completion_tokens"],
#             label="jac (Prompt)" if i == 0 else None,
#             alpha=0.8,
#             color="blue",
#         )

#     # 'dspy' bars
#     if not dspy_data.empty:
#         plt.bar(
#             i + bar_width / 2,
#             dspy_data["completion_tokens"],
#             bar_width,
#             label="dspy (Completion)" if i == 0 else None,
#             alpha=0.8,
#             color="lightgreen",
#         )
#         plt.bar(
#             i + bar_width / 2,
#             dspy_data["prompt_tokens"],
#             bar_width,
#             bottom=dspy_data["completion_tokens"],
#             label="dspy (Prompt)" if i == 0 else None,
#             alpha=0.8,
#             color="green",
#         )

# plt.xlabel("Task", fontsize=14)
# plt.ylabel("Total Tokens", fontsize=14)
# plt.title("Total Token Usage by Task (jac vs dspy)", fontsize=16)
# plt.xticks(
#     [i for i in range(len(ordered_tasks))],
#     ordered_tasks,
#     rotation=45,
#     ha="right",
#     fontsize=12,
# )
# plt.yticks(fontsize=12)
# plt.legend(fontsize=12, loc="upper right")
# plt.tight_layout()
# plt.grid(axis="y", alpha=0.3)

# # Add total token count on top of each bar
# for i, task in enumerate(ordered_tasks):
#     for type, offset in [("jac", -bar_width / 2), ("dspy", bar_width / 2)]:
#         data = total_by_task_type[
#             (total_by_task_type["task"] == task) & (total_by_task_type["type"] == type)
#         ]
#         if not data.empty:
#             total = data["total_tokens"].values[0]
#             plt.text(i + offset, total + 100, f"{total}", ha="center", fontsize=10)

# plt.show()

# # Print out some statistics
# print("Top 5 Token-Intensive Tasks:")
# print(total_by_task.nlargest(5, "total_tokens"))
# print("\n")

# # Calculate total tokens for each type
# total_by_type = df.groupby("type").agg(
#     {"completion_tokens": "sum", "prompt_tokens": "sum", "total_tokens": "sum"}
# )

# print("Total Token Usage by Type:")
# print(total_by_type)
# print("\n")

# # Calculate the percentage of total tokens used by each type
# total_tokens = df["total_tokens"].sum()
# type_percentages = (total_by_type["total_tokens"] / total_tokens) * 100

# print("Percentage of Total Tokens Used by Each Type:")
# print(type_percentages)
# print("\n")

# # Task presence analysis
# tasks_with_both = set(df[df["type"] == "jac"]["task"]) & set(
#     df[df["type"] == "dspy"]["task"]
# )
# tasks_only_jac = set(df[df["type"] == "jac"]["task"]) - tasks_with_both
# tasks_only_dspy = set(df[df["type"] == "dspy"]["task"]) - tasks_with_both

# print("Tasks with Both 'jac' and 'dspy':", tasks_with_both)
# print("Tasks with Only 'jac':", tasks_only_jac)
# print("Tasks with Only 'dspy':", tasks_only_dspy)
