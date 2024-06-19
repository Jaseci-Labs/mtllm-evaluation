import:py dspy ;

with entry {
    llm = dspy.OpenAI(model="gpt-4o");    
    dspy.settings.configure(lm=llm) ;
}

"""Find the Expert Profession to answer the given question."""
class GetExpert:dspy.Signature : {
    has question: str = dspy.InputField(),
        expert: str = dspy.OutputField(desc="Expert Profession");
}

"""Get the Expert's answer to the given question."""
class GetAnswer:dspy.Signature: {
    has question: str = dspy.InputField(),
        expert: str = dspy.InputField(),
        answer: str = dspy.OutputField(desc="Expert's answer");
}

with entry {
    question = "What are Large Language Models?";    
    expert = dspy.Predict(GetExpert)(question=question).expert;    
    answer = dspy.Predict(GetAnswer)(question=question, expert=expert).answer;    
    print(f"{expert} says: {answer}") ;
}

