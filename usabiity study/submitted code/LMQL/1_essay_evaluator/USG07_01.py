import lmql

evaluation_criteria = {
    "clarity": "Does the essay convey its message clearly?",
    "coherency": "Does the essay have a logical flow and coherence?",
    "depth": "Does the essay provide sufficient depth and insight into the topic?",
    "grammar": "Is the essay grammatically correct and well-structured?"
}

essay = f"""
The global power crisis is caused by high energy demand, old infrastructure, and reliance on fossil fuels. 
This crisis results in blackouts, higher costs for businesses, and problems for healthcare and education. 
To fix this, we need to use more renewable energy like solar and wind, update infrastructure, and use energy more efficiently. 
Better governance and regulations can help manage the crisis and attract investments for a stable energy future.
"""

query = f"""
essay: "{essay}"
criteria: "{evaluation_criteria}"

[REMARKS]
[GRADE]
"""

response = lmql.run(query)
remarks = response['REMARKS']
grade = response['GRADE']