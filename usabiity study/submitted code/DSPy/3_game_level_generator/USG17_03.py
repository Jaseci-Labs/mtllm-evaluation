import dspy
from dspy.signatures.signature import signature_to_template


class MapCreater(dspy.Signature):
    """create a new list using the list given and make add more E letters in the middle of B letters if points are higher less E letters if points are lower, B - Block or Obstacles, Enemies and the Player cannot pass through, . - Walkable are for all characters, E - Enemy Character, P - Player Character"""

    oldmap_and_points = dspy.InputField()
    new_map = dspy.OutputField()


# Set up OpenAI model
# turbo = dspy.OpenAI(model='gpt-3.5-turbo', max_tokens=1000)

llm = dspy.OpenAI(model="gpt-4o")
dspy.settings.configure(lm=llm)

new_map_as_template = signature_to_template(MapCreater)


# Define ChainOfThought module
class CoT(dspy.Module):
    def __init__(self):
        super().__init__()
        self.prog = dspy.ChainOfThought(MapCreater)

    def forward(self, map):
        return self.prog(map=map)


# Instantiate CoT module
c = CoT()

old_map = input("Enter your old map : ")

newMap = c.forward(old_map)

print(newMap)
