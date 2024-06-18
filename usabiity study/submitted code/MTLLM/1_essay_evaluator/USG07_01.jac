evaluation_criteria = {
    "clarity": "Does the essay convey its message clearly?",
    "coherency": "Does the essay have a logical flow and coherence?",
    "depth": "Does the essay provide sufficient depth and insight into the topic?",
    "grammar": "Is the essay grammatically correct and well-structured?"
}

essay = """
The global power crisis is caused by high energy demand, old infrastructure, and reliance on fossil fuels. 
This crisis results in blackouts, higher costs for businesses, and problems for healthcare and education. 
To fix this, we need to use more renewable energy like solar and wind, update infrastructure, and use energy more efficiently. 
Better governance and regulations can help manage the crisis and attract investments for a stable energy future.
"""

def evaluate_essay(essay, criteria):
    import by_llm
    lm = by_llm.LLM()

    remarks = lm.generate_remarks(essay, criteria)
    grade = lm.grade_essay(essay, criteria)
    
    return remarks, grade

remarks, grade = evaluate_essay(essay, evaluation_criteria)
print("Evaluator's Remarks:", remarks)
print("Grade:", grade)
