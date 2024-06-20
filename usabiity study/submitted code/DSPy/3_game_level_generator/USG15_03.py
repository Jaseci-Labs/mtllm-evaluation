import dspy

# ollama_model = dspy.OllamaLocal(
#     model="llama2",
#     model_type='text',
#     max_tokens=1500,
#     temperature=0.0,
#     top_p=0.8,
#     frequency_penalty=1.17,
#     top_k=40
# )

# dspy.settings.configure(lm=ollama_model)

llm = dspy.OpenAI(model="gpt-4o")
dspy.settings.configure(lm=llm)


map = [
    'BBBBBBBBBBBBBBBBBBBB',
    'B...E..............B',
    'B.......B..........B',
    'B....BBBB..........B',
    'B..................B',
    'B..................B',
    'B.........P........B',
    'B..................B',
    'B.............E....B',
    'B..................B',
    'B..................B',
    'B.........B........B',
    'B.........B........B',
    'B.........B........B',
    'BBBBBBBBBBBBBBBBBBBB'
]

previous_time_to_win = 5  # Dummy value in minutes
hardness_level = 40  # Dummy value from 1 to 100
win_death_ratio = 2.0  # Dummy value

def generate_harder_map(map, previous_time_to_win, hardness_level, win_death_ratio):
    prompt = f"""
    Given the previous level map:
    {map} of level 50,
    time taken to win level: {previous_time_to_win} minutes,
    hardness level: {hardness_level} in the range of 1-100,
    win/death ratio: {win_death_ratio},
    Predict a new map with structure built on as above but harder.
    The new map should only include the just map and no additional text, intro or explanation.

    Output can contain only following English characters! which have the following meaning
    "B" - Block or Obstacles, Enemies and the Player cannot pass through
    "." - Walkable area for all characters
    "E" - Enemy Character
    "P" - Player Character

    Each line of the map must contain 20! characters
    New map(each on a new line):
    """

    response = llm(prompt)
    new_map = response[0]
    return new_map

new_map = generate_harder_map(map, previous_time_to_win, hardness_level, win_death_ratio)

print(new_map)
