import lmql

# Initialize LMQL engine
lmql_engine = lmql.Engine()


def evaluateEssay(essay, criteria):
    """
    Evaluate the given essay based on the provided criteria.
    Return detailed remarks.
    """
    query = f"""
    Evaluate the essay based on the {criteria}:
    {essay}
    [JUDGEMENT]
    """
    response = lmql_engine.query(query, temperature=0.7)
    return response["JUDGEMENT"]


def generateRemark(essay, judgements):
    """
    Generate a summary of the provided judgments for the essay.
    """
    judgements_str = "\n".join(
        [f"{criteria}: {judgment}" for criteria, judgment in judgements.items()]
    )
    query = f"""
    Generate a review based on judgments:
    {judgements_str}
    {essay}
    [REMARK]
    """
    response = lmql_engine.query(query, temperature=0.7)
    return response["REMARK"]


def generateGrade(review):
    """
    Based on the review, .
    """
    query = f"""
    Determine the grade based on the REVIEW:
    {review}
    [GRADE]
    """
    response = lmql_engine.query(query, temperature=0.7)
    return response["GRADE"]


def main():
    essay = input("Enter the essay here: ")

    criterias = [
        "Clarity",
        "Coherence",
        "Originality",
        "Evidence",
        "Correct Spelling and grammar",
    ]  # can be extended
    judgements = {}

    # Evaluate essay based on criteria
    for criteria in criterias:
        judgement = evaluateEssay(essay, criteria)
        judgements[criteria] = judgement

    # Generate summary of judgments
    remark = generateRemark(essay, judgements)

    # Determine grade based on summary
    grade = generateGrade(remark)

    print("Reviewer Remarks:", remark)
    print("Grade:", grade)


if _name_ == "_main_":
    main()
