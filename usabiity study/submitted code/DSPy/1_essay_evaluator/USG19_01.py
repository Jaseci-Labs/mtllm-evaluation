import dspy


class EvaluateEssay(dspy.Signature):
    """Evaluate an essay and assign a grade."""

    essay = dspy.InputField(desc="the essay to be evaluated")
    remarks = dspy.OutputField(desc="evaluation remarks")
    grade = dspy.OutputField(desc="grade assigned to the essay")


class GenerateRemarks(dspy.Signature):
    """Generate evaluation remarks based on the content of the essay."""

    essay = dspy.InputField(desc="the essay content")
    remarks = dspy.OutputField(desc="evaluation remarks")


class EssayEvaluator(dspy.Module):
    def __init__(self):
        super().__init__()

        self.generate_remarks = dspy.ChainOfThought(GenerateRemarks)

    def forward(self, essay):
        remarks = self.generate_remarks(essay=essay).remarks

        # Logic to assign a grade based on the evaluation remarks
        # This can be a simple if-else condition or a more complex scoring mechanism

        # For demonstration purposes, let's assume a simple grading scheme
        if "well-written" in remarks and "insightful" in remarks:
            grade = "A"
        elif "adequate" in remarks and "clear" in remarks:
            grade = "B"
        elif "needs improvement" in remarks:
            grade = "C"
        else:
            grade = "F"

        return dspy.Prediction(remarks=remarks, grade=grade)


teleprompter = dspy.teleprompt.BootstrapFewShot(metric=None)
compiled_evaluator = teleprompter.compile(EssayEvaluator(), trainset=trainset)

evaluate_on_essays = Evaluate(devset=essay_devset, num_threads=1, display_progress=True)
evaluation_score = evaluate_on_essays(compiled_evaluator, metric=None)
print(f"Evaluation Score: {evaluation_score}")
