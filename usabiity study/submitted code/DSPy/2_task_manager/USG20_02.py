from dspy import DSPy

dspy = DSPy()


def evaluate_essay(essay, criteria):
    response = dspy.process(
        f"Evaluate the following essay based on the criteria: {criteria}\n\nEssay:\n{essay}\n\nProvide evaluator's remarks and grade it from A, B, C, D, S, F."
    )
    remarks = response["remarks"]
    grade = response["grade"]
    return remarks, grade


essay_text = """The global power crisis is caused by high energy demand, old infrastructure, and reliance on fossil fuels. This crisis results in blackouts, higher costs for businesses, and problems for healthcare and education. To fix this, we need to use more renewable energy like solar and wind, update infrastructure, and use energy more efficiently. Better governance and regulations can help manage the crisis and attract investments for a stable energy future."""
criteria = "Clarity, Coherency, Argument strength, Grammar and syntax, Overall impact"

remarks, grade = evaluate_essay(essay_text, criteria)
print(f"Remarks: {remarks}\nGrade: {grade}")
