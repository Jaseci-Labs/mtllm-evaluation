import lmql

@lmql.query
def get_answer(question, query: str) -> int:
    """lmql
    "Return the correct result for the given math problem.\n"
    "Math Problem: {question}\n"
    "Answer: [answer]" where STOPS_AT(answer, ".")
    return judgement
    """
question = input()
response = get_answer(question)
print(response.answer)