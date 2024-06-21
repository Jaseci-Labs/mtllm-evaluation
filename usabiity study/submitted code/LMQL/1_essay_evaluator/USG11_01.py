import lmql


def evaluate(essay, criteria):
    """
    Evaluate the given essay based on the provided criteria.
    Return detailed remarks.
    """
    query = f"""
    Evaluate the given essay based on the following criteria: {criteria}
    Provide detailed judgment.
    Essay: {essay}
    [REMARKS]
    """
    return lmql.query(query, temperature=0.7).text


def remark(essay, judgements):
    """
    Generate a summary of the provided judgments for the essay.
    """
    judgements_str = "\n".join(
        [f"{criteria}: {judgment}" for criteria, judgment in judgements.items()]
    )
    query = f"""
    Generate a summary of the following judgments:
    {judgements_str}
    Essay: {essay}
    [SUMMARY]
    """
    return lmql.query(query, temperature=0.7).text


def grading(summary):
    """
    Based on the summary, give a letter grade out of [A,B,C,S,F].
    """
    query = f"""
    Based on the following summary, give a letter grade out of [A,B,C,S,F]:
    {summary}
    [GRADE]
    """
    return lmql.query(query, temperature=0.7).text


def main():

    essay = input("Enter the eassay here : ")

    criterias = [
        "Clarity",
        "Coherence",
        "Originality",
        "Evidence",
        "Correct Spelling and grammar",
    ]  # can be extended
    judgements = {}

    # Judgements
    for criteria in criterias:
        judgement = evaluate(essay, criteria)
        judgements[criteria] = judgement

    remark = remark(essay, judgements)
    grade = grading(remark)

    print("Reviewer Remark:", remark)
    print("Grade:", grade)


if __name__ == "__main__":
    main()
