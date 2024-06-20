# Import the Jac module
from jac import Jac

# Initialize Jac with the LLM feature
jac = Jac()

def evaluate_essay(essay, criteria):
    # Create a query to evaluate the essay based on the given criteria
    query = f"""
    Evaluate the following essay based on the criteria: {criteria}

    Essay:
    {essay}

    Provide evaluator's remarks and grade it from A, B, C, D, S, F."""
    # Use the LLM feature of Jac to process the query
    response = jac.llm_evaluate(query)
    # Extract the remarks and grade from the response
    remarks = response.get('remarks', 'No remarks provided.')
    grade = response.get('grade', 'No grade provided.')  
    return remarks, grade

# Example essay text
essay_text = "The global power crisis is caused by high energy demand, old infrastructure, and reliance on fossil fuels. This crisis results in blackouts, higher costs for businesses, and problems for healthcare and education. To fix this, we need to use more renewable energy like solar and wind, update infrastructure, and use energy more efficiently. Better governance and regulations can help manage the crisis and attract investments for a stable energy future."

# Evaluation criteria
criteria = "Clarity, Coherency, Argument strength, Grammar and syntax, Overall impact"

# Evaluate the essay using the criteria
remarks, grade = evaluate_essay(essay_text, criteria)

# Print the results
print(f"Remarks: {remarks}\nGrade: {grade}")