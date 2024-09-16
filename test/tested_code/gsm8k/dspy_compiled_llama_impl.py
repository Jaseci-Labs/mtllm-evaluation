from dspy_compilation import CoT
import os
import dspy

model_name = os.environ["MODEL_NAME"]
llm = dspy.OllamaLocal(
    model=model_name, base_url="http://141.212.106.90:8080", timeout_s=1200
)
dspy.configure(lm=llm)
program = CoT
CoT.load("optimized.json")
question = input()
answer = CoT(question=question).answer
print(answer)
