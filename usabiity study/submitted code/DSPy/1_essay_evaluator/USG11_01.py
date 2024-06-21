import dspy

# phi3 = dspy.OllamaLocal(model="phi3")
llm = dspy.OpenAI(model="gpt-4o")
dspy.settings.configure(lm=llm)

essay = input("Write your essay here: ")
criteria_list = [
    "Clarity",
    "Coherence",
    "Originality",
    "Evidence",
    "Correct Spelling and Grammar",
]
criteria = ", ".join(criteria_list)  # Convert list to a comma-separated string


class EssayEvaluation(dspy.Signature):
    essay: str = dspy.InputField()
    criteria: str = dspy.InputField()
    remark: str = dspy.OutputField()


class Grading(dspy.Signature):
    reviewer_remark: str = dspy.InputField()
    possible_grades: str = (
        dspy.InputField()
    )  # Added to include the possible grades in the input
    grade: str = dspy.OutputField()


with dspy.context(lm=llm):
    # Evaluate the essay
    evaluation = dspy.Predict(EssayEvaluation)(essay=essay, criteria=criteria)
    reviewer_remark = evaluation.remark.split("Remark: ")[-1].strip()
    print("Reviewer's Remark:", reviewer_remark)

    # Grade the essay
    possible_grades = "A, B, C, S, F"
    grading = dspy.Predict(Grading)(
        reviewer_remark=reviewer_remark, possible_grades=possible_grades
    )
    grade = grading.grade.split("Grade: ")[-1].strip()
    print("Grade:", grade)
