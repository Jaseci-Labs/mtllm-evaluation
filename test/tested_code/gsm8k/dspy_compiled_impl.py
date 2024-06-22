from dspy_compilation import CoT
import os
import dspy

model_name = os.environ["MODEL_NAME"]
llm = dspy.OpenAI(model=model_name, max_tokens=1000)
dspy.configure(lm=llm)
program = CoT
CoT.load("optimized.json")
answer = CoT(question="What is 1+1").answer
print(answer)