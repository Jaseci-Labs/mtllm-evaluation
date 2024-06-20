from transformers import pipeline

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

model_name = "text-davinci-003"  # Example model from OpenAI
llm_pipeline = pipeline('text-generation', model=model_name)

def generate_evaluation(essay, criteria):
    prompt = f"""
    Evaluate the following essay based on the given criteria:

    Essay: {essay}

    Criteria:
    - Clarity: {criteria['clarity']}
    - Coherency: {criteria['coherency']}
    - Depth: {criteria['depth']}
    - Grammar: {criteria['grammar']}

    Provide detailed remarks and a grade (A, B, C, D, S, F).
    """
    
    response = llm_pipeline(prompt, max_length=500, num_return_sequences=1)
    output = response[0]['generated_text']
    
    remarks, grade = output.split("Grade:")
    return remarks.strip(), grade.strip()

remarks, grade = generate_evaluation(essay, evaluation_criteria)

print("Evaluator's Remarks:", remarks)
print("Grade:", grade)