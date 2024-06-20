from dsp import LM
import requests
import dspy

claude_model = Anthropic(model="claude-3-sonnet-20240229")
dspy.configure(lm=claude_model)

llm = dspy.OpenAI(model="gpt-4o")
dspy.settings.configure(lm=llm)

class MapGenerate(dspy.Signature):
    """Generate the next map based on the parameters.
    Next map should have the same structure as current map but harder.
    "B"-Block or Obstacles, Enemies and the Player cannot pass through, "."-Walkable area for all characters, "E"-Enemy Character(can have many), "P"-Player Character.There should be only one player
    Give the map only"""

    current_map = dspy.InputField()
    other_parameters = dspy.InputField()

    next_map = dspy.OutputField(desc="Next Map Structure")

class CoT(dspy.Module):
    def __init__(self):
        super().__init__()
        self.prog = dspy.ChainOfThought(MapGenerate)

    def forward(self, current_map, other_parameters):
        return self.prog(current_map=current_map, other_parameters=other_parameters)

c = CoT()

map = """
    "BBBBBBBBBBBBBBBBBBBBB",
    "B.............E....B",
    "B...........B......B",
    "B........BBBB......B",
    "B..................B",
    "B..................B",
    "B..................B",
    "B.......P..........B",
    "B..................B",
    "B..........E.......B",
    "B..................B",
    "B..................B",
    "B..................B",
    "B.....B............B",
    "B.....B............B",
    "BBBBBBBBBBBBBBBBBBBBB"
"""

parameters = """
            time taken to win current level: 2 minutes,
            hardness level (1-100): 40,
            win/death ratio: 5/3
            """

next_map = c.forward(map, parameters)

print(next_map['next_map'])
