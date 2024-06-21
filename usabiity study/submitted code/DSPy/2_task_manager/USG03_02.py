import dspy

# Setup Ollama environment
ollama_mistral = dspy.OllamaLocal(model="phi3:3.8b")
dspy.settings.configure(lm=ollama_mistral)

llm = dspy.OpenAI(model="gpt-4o")
dspy.settings.configure(lm=llm)


class EvaluateEssay(dspy.Signature):
    """Evaluate the Essay based on criteria and grade it as A,B,D,S,F"""

    Criteria = dspy.InputField()
    Evaluation = dspy.OutputField(desc="Give the grade")
    Remarks = dspy.OutputField(desc="Give the review based on criteria")


Essay = "The 21-year-old made seven appearances for the Hammers and netted his only goal for them in a Europa League qualification round match against Andorran side FC Lustrains last season. Lee had two loan spells in League One last term, with Blackpool and then Colchester United. He scored twice for the U's but was unable to save them from relegation. The length of Lee's contract with the promoted Tykes has not been revealed. Find all the latest football transfers on our dedicated page."

Criteria = "clarity, coherency"

Evaluation = dspy.Predict(EvaluateEssay)
print(Evaluation(Essay=Essay, Criteria=Criteria))
