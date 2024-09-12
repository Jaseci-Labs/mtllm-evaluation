import dspy
import os
model_name = os.environ["MODEL_NAME"]
llm = dspy.OllamaLocal(model=model_name, max_tokens=1000, base_url="http://141.212.106.90:8080")
dspy.configure(lm=llm)
question = input()
answer = dspy.TypedChainOfThought('question:str -> answer:int', max_retries=1)
response = answer(question=question)

print(response.answer)
