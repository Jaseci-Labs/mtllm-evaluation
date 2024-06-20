obj EssayEvaluationInput {
    has essay: str;
    has evaluation_criteria: dict[str, float];
}

obj EssayEvaluationOutput {
    has evaluator_remarks: str;
    has grade: str;
}
obj EssayEvaluator {
    can evaluate_essay(input: EssayEvaluationInput) -> EssayEvaluationOutput {
        # Extract input
        essay = input.essay
        criteria = input.evaluation_criteria

        # Evaluation logic
        clarity = criteria.get("clarity", 0.0)
        coherency = criteria.get("coherency", 0.0)

        remarks = ""

        if clarity >= 0.8 and coherency >= 0.8:
            remarks = "Well-written and insightful."
            grade = "A"
        elif clarity >= 0.7 and coherency >= 0.7:
            remarks = "Adequate and clear."
            grade = "B"
        else:
            remarks = "Needs improvement."
            grade = "F"

        return EssayEvaluationOutput(evaluator_remarks=remarks, grade=grade)
    }
}
# Example essay and evaluation criteria
example_essay = "The global power crisis is caused by high energy demand, old infrastructure, and reliance on fossil fuels. This crisis results in blackouts, higher costs for businesses, and problems for healthcare and education. To fix this, we need to use more renewable energy like solar and wind, update infrastructure, and use energy more efficiently. Better governance and regulations can help manage the crisis and attract investments for a stable energy future."

evaluation_criteria = {
    "clarity": 0.75,
    "coherency": 0.85
}

# Evaluate the essay
evaluation_input = EssayEvaluationInput(essay=example_essay, evaluation_criteria=evaluation_criteria)
evaluation_output = EssayEvaluator.evaluate_essay(evaluation_input)

# Print the results
print("Evaluator's Remarks:", evaluation_output.evaluator_remarks)
print("Grade:", evaluation_output.grade)
