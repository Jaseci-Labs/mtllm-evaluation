import dspy

phi3 = dspy.OllamaLocal(model="phi3")

llm = dspy.OpenAI(model="gpt-4o")
dspy.settings.configure(lm=llm)


previous_level_map = [
    "WWWWWWWWWWWW",
    "W.........WW",
    "W..WWWWWW..W",
    "W..........W",
    "W..W....W..W",
    "W..........W",
    "WWWWWWWWWWWW",
]
n = len(previous_level_map)

class LevelUp(dspy.Signature):
    previous_level_map: list[str] = dspy.InputField(desc="A map of the previous level of the game")
    time_taken: str = dspy.InputField(desc="Time taken to play the game")
    win_death_ratio: str = dspy.InputField(desc="Winning or dying ratio")
    hardness_level: str = dspy.InputField(desc="Hardness level")
    next_level_map: list[str] = dspy.OutputField(desc="Make the game harder and the map should have only B (for blocks), E (for enimies), P (for player and only one P should be there) and . (for walkable) It should have 84 elements")

with dspy.context(lm=llm):
    level_up = dspy.Predict(LevelUp)(
        previous_level_map="".join(previous_level_map),
        time_taken=str(120),
        win_death_ratio=str(3),
        hardness_level=str(70)
    )
    new_level_map = level_up.next_level_map.split("\n")[0].split(":")[1].lstrip()

n_elements = 7
length_of_each = 12

substrings = [
    new_level_map[i : i + length_of_each]
    for i in range(0, n_elements * length_of_each, length_of_each)
]

for element in substrings:
    print(element)
