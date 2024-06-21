import lmql

# Define the grading criteria
grading_criteria = {
    "grammar": {"weight": 0.3, "criteria": ["grammar", "spelling", "punctuation"]},
    "content": {"weight": 0.5, "criteria": ["clarity", "relevance", "depth"]},
    "structure": {"weight": 0.2, "criteria": ["organization", "coherence"]},
}

# Define the essay to be evaluated
essay = """The global power crisis is caused by high energy demand, old infrastructure, and reliance on fossil fuels.
            This crisis results in blackouts, higher costs for businesses, and problems for healthcare and education.
             To fix this, we need to use more renewable energy like solar and wind, update infrastructure, and use energy
             more efficiently. Better governance and regulations can help manage the crisis and attract investments for
             a stable energy future."""

# Create an LMQL model
model = lmql.LMQL(grading_criteria)

# Evaluate the essay
grades = model.evaluate(essay)

# Print the grades
print("Grades:")
for criterion, grade in grades.items():
    print(f"{criterion.capitalize()}: {grade}")

# Calculate the overall grade
overall_grade = sum(grade * criteria["weight"] for criterion, grade in grades.items())
print(f"\nOverall Grade: {overall_grade:.2f}")
