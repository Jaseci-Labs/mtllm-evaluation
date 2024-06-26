from dspy_compilation import CoT
import os
import dspy

model_name = os.environ["MODEL_NAME"]
llm = dspy.OpenAI(model=model_name, max_tokens=2000)
dspy.configure(lm=llm)
program = CoT
CoT.load("optimized.json")
question = input()
answer = CoT(question=question).answer
print(answer)