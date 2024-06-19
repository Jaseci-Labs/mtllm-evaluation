import lmql

def evaluate_essay(essay, criteria):  #evaluation
    return lmql.query(f"""
    Evaluate the given essay based on the following criteria: {criteria}
    Provide Detailed Judgement.
    Essay: {essay}
    [REMARKS]
    """, temperature=0.7).text

def generate_summary(essay, judgements): #summary of evaluations based on different criterion
    return lmql.query(f"""
    Generate a summary of the following judgements:
    {judgements}
    Essay: {essay}
    [SUMMARY]
    """, temperature=0.7).text

def give_grade(summary):
    return lmql.query(f"""
    Based on the following summary, give a letter grade (A-D):
    {summary}
    [GRADE]
    """, temperature=0.7).text

def main():
    essay = """
    With a population of approximately 45 million Spaniards and 3.5 million immigrants,
    Spain is a country of contrasts where the richness of its culture blends it up with
    the variety of languages and dialects used. Being one of the largest economies worldwide,
    and the second largest country in Europe, Spain is a very appealing destination for tourists
    as well as for immigrants from around the globe. Almost all Spaniards are used to speaking at
    least two different languages, but protecting and preserving that right has not been
    easy for them. Spaniards have had to struggle with war, ignorance, criticism and the governments,
    in order to preserve and defend what identifies them, and deal with the consequences.
    """

    criterias = ["Clarity", "Originality", "Evidence", "Coherence and Organization", "Grammar and Syntax", "Overall Impression"] #can be extended
    judgements = {}

    #Judgements
    for criteria in criterias:
        judgement = evaluate_essay(essay, criteria)
        judgements[criteria] = judgement

    summary = generate_summary(essay, judgements)

    grade = give_grade(summary)

    print("Reviewer Notes:", summary)
    print("Grade:", grade)

main()