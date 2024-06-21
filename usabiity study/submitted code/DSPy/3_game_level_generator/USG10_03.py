import dspy

# phi3 = dspy.dspy.OllamaLocal(model="phi3:3.8b")

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

# Convert the list of strings into a single string
previous_level_str = "\n".join(previous_level_map)


class LevelUp(dspy.Signature):
    """Build a next level map which has the same dimensions as the previous_level_map"""

    previous_level_map: str = dspy.InputField(
        desc="A map of the previous level of the game"
    )
    time_taken: str = dspy.InputField(desc="Time taken to play the game")
    win_death_ratio: str = dspy.InputField(desc="Winning or dying ratio")
    hardness_level: str = dspy.InputField(desc="Hardness level (0-100)")
    next_level_map: list[str] = dspy.OutputField(
        desc="Make the game harder and the map should have only B(for blocks), E(for enemies), P(for player and only one P should be there) and .(for walkable).It should not include spaces("
        ") It should have only 144 elements"
    )


with dspy.context(lm=llm):
    level_up = dspy.Predict(LevelUp)(
        previous_level_map=previous_level_str,
        time_taken="60",
        win_death_ratio="2.5",
        hardness_level="80",
    )
    new_level_map = level_up.next_level_map


new_map = [new_level_map[i : i + 12] for i in range(0, 144, 12)]

for element in new_map:
    print(element)

print(new_level_map)
