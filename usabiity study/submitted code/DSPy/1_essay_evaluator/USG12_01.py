import dspy

class Evaluation(dspy.Signature):
    """Evaluation of paragraph based on provided criteria"""
    
    text:str = dspy.InputField()
    assessment:str = dspy.OutputField()

# Paragraph to be evaluated
paragraph_text = """The global power crisis is caused by high energy demand, old infrastructure, 
    and reliance on fossil fuels. This crisis results in blackouts, higher costs 
    for businesses, and problems for healthcare and education. To fix this, we need 
    to use more renewable energy like solar and wind, update infrastructure, and use 
    energy more efficiently. Better governance and regulations can help manage the crisis 
    and attract investments for a stable energy future."""

# Configure the local model
# local_model = dspy.OllamaLocal(model='phi3:3.8b')
# dspy.settings.configure(lm=local_model)

llm = dspy.OpenAI(model="gpt-4o")
dspy.settings.configure(lm=llm)

# Evaluation criteria
criteria_text = "Evaluate based on clarity, grammar, organization, and content. Grade the paragraph using A for the best, B for good, C for satisfactory, D for low pass, S for marginal failure, and F for failure. Give reasoning for your choice in grade."

def perform_evaluation(criteria, paragraph):
    Evaluation._doc_ = criteria
    evaluator = dspy.Predict(Evaluation)
    result = evaluator(text=paragraph)
    return result.assessment

# Perform the evaluation and print the result
evaluation_result = perform_evaluation(criteria_text, paragraph_text)
print(evaluation_result)
