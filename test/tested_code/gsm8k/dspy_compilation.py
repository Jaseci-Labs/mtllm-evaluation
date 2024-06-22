import dspy
import dspy.datasets
from dspy.datasets import GSM8K
import dspy.teleprompt
from datasets import load_dataset

CoT = dspy.TypedChainOfThought("question -> answer:int") 
if __name__ == "__main__":
  train = GSM8K().test
  fewshot = dspy.teleprompt.LabeledFewShot(k=8).compile(CoT, trainset=train)
  fewshot.save("optimized.json")