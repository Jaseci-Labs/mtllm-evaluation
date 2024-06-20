import dspy

# phi3 = dspy.OllamaLocal(model="phi3")

llm = dspy.OpenAI(model="gpt-4o")
dspy.settings.configure(lm=llm)


previous_level_map = [
    "BBBBBBBBBBBB",
    "B.........BB",
    "B..BBBBB...B",
    "B...PB.....B",
    "B..BE.E...BB",
    "B..........B",
    "BBBBBBBBBBBB",
]
n = len(previous_level_map)


class LevelUp(dspy.Signature):
    """Build a next level map which has the same dimensions as the previous_level_map"""

    previous_level_map: list[str] = dspy.InputField(
        desc="A map of the previous level of the game"
    )
    time_taken: str = dspy.InputField(desc="Time taken to play the game")
    win_death_ratio: str = dspy.InputField(desc="Winning or dying ratio")
    hardness_level: str = dspy.InputField(desc="Hardness level")
    next_level_map: list[str] = dspy.OutputField(
        desc="Make the game harder and the map should have only B (for blocks), E (for enimies), P (for player and only one P should be there) and . (for walkable) It should have 84 elements"
    )


with dspy.context(lm=llm):
    level_up = dspy.Predict(LevelUp)(
        previous_level_map="".join(previous_level_map),
        time_taken=str(120),  # Convert to string
        win_death_ratio=str(3),  # Convert to string
        hardness_level=str(70),  # Convert to string
    )
    new_level_map = level_up.next_level_map.split("\n")[0].split(":")[1].lstrip()

n_elements = 7
length_of_each = 12

# Split the string into substrings of length length_of_each
substrings = [
    new_level_map[i : i + length_of_each]
    for i in range(0, n_elements * length_of_each, length_of_each)
]

for element in substrings:
    print(element)
