import llama2

def evaluate_essay(essay, criteria):
    criteria_str = ", ".join(criteria)
    prompt = f"""
    Evaluate the following essay based on the criteria provided:

    Essay: {essay}

    Criteria for evaluation: {criteria_str}

    Please provide detailed evaluator remarks for the essay based on the given criteria and assign a grade (A, B, C, D, S, F).

    Evaluator's Remarks:
    """

    result = llama2.generate(
        prompt=prompt,
        max_tokens=300,
        temperature=0.7
    )
    
    remarks = result['text']
    grade = remarks.split()[-1] if remarks.split()[-1] in ['A', 'B', 'C', 'D', 'S', 'F'] else 'N/A'
    
    return remarks, grade

essay = "The global power crisis is caused by high energy demand, old infrastructure, and reliance on fossil fuels. This crisis results in blackouts, higher costs for businesses, and problems for healthcare and education. To fix this, we need to use more renewable energy like solar and wind, update infrastructure, and use energy more efficiently. Better governance and regulations can help manage the crisis and attract investments for a stable energy future."
criteria = ["clarity", "coherence", "grammar", "relevance", "structure"]

remarks, grade = evaluate_essay(essay, criteria)

print("Evaluator's Remarks:\n", remarks)
print("\nGrade:", grade)
