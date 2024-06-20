import lmql

@lmql.query
def evaluate_essay(essay: str):
    '''lmql
    argmax
    "Generate a brief remark for the following essay: " + essay
    clause

    argmax
    "Grade the essay with A, B, C, S, or F: " + essay
    clause
    '''

essay = "This is a sample essay to test the evaluation system."
evaluation = evaluate_essay(essay)
print(evaluation)
