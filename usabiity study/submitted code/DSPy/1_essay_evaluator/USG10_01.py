import dspy

# phi3 = dspy.dspy.OllamaLocal(model="phi3:3.8b")

llm = dspy.OpenAI(model="gpt-4o")
dspy.settings.configure(lm=llm)


essay = input("Write your essay here: ")


class EssayEvaluation(dspy.Signature):
    """According to Clarity,  Coherence , Originality , Evidence , depth , Correct Spelling and Grammar criterias evaluate the provided essay."""

    essay: str = dspy.InputField()
    remark: str = dspy.OutputField()


class Grading(dspy.Signature):
    """Give a Grade from these grades only using A,B,C,S and F"""

    reviewer_remark: str = dspy.InputField()
    grade: str = dspy.OutputField()


with dspy.context(lm=llm):
    # Evaluate the essay
    evaluation = dspy.Predict(EssayEvaluation)(essay=essay)
    reviewer_remark = evaluation.remark.split("Remark: ")[-1].strip()

    # Grade the essay

    grading = dspy.Predict(Grading)(reviewer_remark=reviewer_remark)
    grade = grading.grade
    print(grade)
