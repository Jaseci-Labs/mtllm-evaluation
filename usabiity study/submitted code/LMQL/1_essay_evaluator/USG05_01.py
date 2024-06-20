import lmql

# Define the evaluation criteria and grade ranges
evaluation_criteria = """
    Thesis Statement (0-10 marks), 
    Clarity of Argument (0-10 marks), 
    Organization (0-10 marks), 
    Supporting Evidence (0-10 marks), 
    Analysis and Critical Thinking (0-10 marks), 
    Use of Language (0-10 marks), 
    Grammar and Mechanics (0-10 marks), 
    Originality and Creativity (0-10 marks), 
    Engagement of the Reader (0-10 marks), 
    Conclusion (0-10 marks)
    """

grade_ranges = "A (if marks 100-75), B (if marks 74-65), C (if marks 64-55), S (if marks 54-35), F (if marks 34-0)"

# Sample essay
entered_essay = """
    Reading enriches our lives by exposing us to new ideas and perspectives. 
    It improves our vocabulary, enhances communication skills, and boosts cognitive functions. 
    By fostering empathy and expanding our knowledge, reading is a simple yet powerful tool for personal growth.
    """

# Define the LMQL query
query = f"""
argmax
    "Evaluate the essay based on the given criteria and provide a detailed evaluation."
    evaluate_essay(essay: {entered_essay}, criteria: {evaluation_criteria}) -> evaluation

    "Based on the evaluation details, give a grade letter (A,B,C,S,F)."
    grade_essay(evaluation: evaluation, grading_range: {grade_ranges}) -> grade

    "Generate a small remark with important points."
    remark_essay(evaluation: evaluation, grade: grade) -> remark

from
    llm('openai/gpt-3.5-turbo-instruct')
"""


# Execute the query
response = lmql.run(query)

# Extract the evaluation, grade, and remark from the response
evaluation = response["evaluate_essay"]
grade = response["grade_essay"]
remark = response["remark_essay"]

# Print the results
print("Evaluation:", evaluation)
print("Grade:", grade)
print("Remark:", remark)