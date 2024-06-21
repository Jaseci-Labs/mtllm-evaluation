import dspy


class Grade(dspy.Signature):
    """test"""

    sentence = dspy.InputField()
    grade = dspy.OutputField()


sentence = """
    The global power crisis is caused by high energy demand, old infrastructure, 
    and reliance on fossil fuels. This crisis results in blackouts, higher costs 
    for businesses, and problems for healthcare and education. To fix this, we need 
    to use more renewable energy like solar and wind, update infrastructure, and use 
    energy more efficiently. Better governance and regulations can help manage the crisis 
    and attract investments for a stable energy future."""

# ollama_mistral = dspy.OllamaLocal(model='phi3:3.8b')
# dspy.settings.configure(lm=ollama_mistral)

llm = dspy.OpenAI(model="gpt-4o")
dspy.settings.configure(lm=llm)


cri = "Evaluate based on clarity,Grammar, Sentence structure, Organization and content. Grade the sentence using A for the best, B for the good, C for the Satisfactory, D for the Low Pass, but certifying, S for the Low Failure and F for the Failure.  Give reasoning for your choice in grade "


def performTask(criteria, para):
    Grade.__doc__ = criteria
    classify = dspy.Predict(Grade)
    x = classify(sentence=para)
    return x.grade


y = performTask(cri, sentence)
print(y)
