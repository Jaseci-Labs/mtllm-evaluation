import lmql


@lmql.query(beams=2)
def expert_answer(question):
    """lmql
    "Q: {question}\n\n"

    # prompt for an 'expert'
    "A good person to answer this question would be[EXPERT]\n\n" where \
        STOPS_AT(EXPERT, ".") and STOPS_AT(EXPERT, "\n")
    expert_name = EXPERT.rstrip(".\n")

    # use 'expert' to answer the question
    "For instance,{expert_name} would answer[ANSWER]" where STOPS_AT(ANSWER, ".")
    return f'{expert_name} says: {ANSWER}'
    """


print(expert_answer("What are Large Language Models?"))
