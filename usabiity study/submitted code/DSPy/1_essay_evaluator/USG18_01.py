import dspy

# phi3 = dspy.OllamaLocal(model="phi3")
llm = dspy.OpenAI(model="gpt-4o")
dspy.settings.configure(lm=llm)

# Hardcoded essay
essay = """
Artificial intelligence (AI) is rapidly transforming the world we live in. From self-driving cars to virtual assistants,
AI technologies are becoming an integral part of our daily lives. The ability of machines to learn and adapt is revolutionizing
industries and improving efficiency. However, this rapid advancement also raises ethical concerns about job displacement and privacy.
The key to harnessing AI's potential lies in balancing innovation with responsible development, ensuring that AI benefits all of humanity
while mitigating its risks.
"""

criteria_list = [
    "Clarity",
    "Originality",
    "Evidence",
    "Coherence and Organization",
    "Grammar and Syntax",
    "Overall Impression",
]
criteria = ", ".join(criteria_list)  # Convert list to a comma-separated string


class EvaluateEssay(dspy.Signature):
    essay: str = dspy.InputField()
    criteria: str = dspy.InputField()
    remark: str = dspy.OutputField()


class GiveGrade(dspy.Signature):
    reviewer_remark: str = dspy.InputField()
    possible_grades: str = dspy.InputField()
    grade: str = dspy.OutputField()


with dspy.context(lm=llm):
    # Evaluate the essay
    evaluation = dspy.Predict(EvaluateEssay)(essay=essay, criteria=criteria)
    reviewer_remark = evaluation.remark.split("Remark: ")[-1].strip()
    print("Reviewer's Remark:", reviewer_remark)

    # Grade the essay
    possible_grades = "A, B, C, S, F"
    grading = dspy.Predict(GiveGrade)(
        reviewer_remark=reviewer_remark, possible_grades=possible_grades
    )
    grade = grading.grade.split("Grade: ")[-1].strip()
    print("Grade:", grade)
