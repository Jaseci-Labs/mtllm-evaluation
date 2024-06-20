import lmql

@lmql.query(model="openai/gpt-3.5-turbo-instruct", decoder="argmax")
def review_essay(essay, criteria):
    '''lmql
    Review the following essay based on the criteria provided and give an overall evaluation and grade (A, B, C, D, S, F).

    Essay: [ESSAY]

    Criteria: [CRITERIA]

    Evaluator's Remarks:
    [REMARKS]
    Grade: [GRADE]""" where STOPS_AT(REMARKS, "\n") and GRADE in set(["A", "B", "C", "D", "S", "F"])
    '''

# Example usage:
essay = "The global power crisis is caused by high energy demand, old infrastructure, and reliance on fossil fuels. This crisis results in blackouts, higher costs for businesses, and problems for healthcare and education. To fix this, we need to use more renewable energy like solar and wind, update infrastructure, and use energy more efficiently. Better governance and regulations can help manage the crisis and attract investments for a stable energy future."

criteria = "Clarity, coherence, argument strength, evidence support, and overall impact."

result = review_essay(essay, criteria)
print("Evaluator's Remarks: ", result.REMARKS)
print("Grade: ", result.GRADE)
