import dspy

llm = dspy.OpenAI(model="gpt-4o")
dspy.settings.configure(lm=llm)


class GetExpert(dspy.Signature):
    """Find the Expert Profession to answer the given question."""

    question: str = dspy.InputField()
    expert: str = dspy.OutputField(desc="Expert Profession")


class GetAnswer(dspy.Signature):
    """Get the Expert's answer to the given question."""

    question: str = dspy.InputField()
    expert: str = dspy.InputField()
    answer: str = dspy.OutputField(desc="Expert's answer")


question = "Who is the first Man on Earth?"
expert = dspy.Predict(GetExpert)(question=question).expert
answer = dspy.Predict(GetAnswer)(question=question, expert=expert).answer
print(f"{expert} says: {answer}")
