import dspy

turbo = dspy.OpenAI(model="gpt-3.5-turbo")
dspy.settings.configure(lm=turbo)


class GetExpert(dspy.Signature):
    """Find the Expert Profession to answer the given question."""

    question: str = dspy.InputField()
    expert: str = dspy.OutputField(desc="Expert Profession")


class GetAnswer(dspy.Signature):
    """Get the Expert's answer to the given question."""

    question: str = dspy.InputField()
    expert: str = dspy.InputField()
    answer: str = dspy.OutputField(desc="Expert's answer")


question = "What are Large Language Models?"
expert = dspy.Predict(GetExpert)(question=question).expert
answer = dspy.Predict(GetAnswer)(question=question, expert=expert).answer
print(f"{expert} says: {answer}")
