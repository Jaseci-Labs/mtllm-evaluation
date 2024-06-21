# failed to generate tokens 'The requested number of tokens exceeds the llama.cpp model's context size. Please specify a higher n_ctx value.''

import lmql

llm = lmql.model("openai/gpt-3.5-turbo-instruct")


class Map:
    def __init__(self, content):
        self.content = content

    def __str__(self):
        return "\n".join(self.content)


@lmql.query(model=llm, lang="en")
def generate_harder_map(
    map_content, previous_time_to_win, hardness_level, win_death_ratio
):
    """lmql
    "Q: Given the previous level map: '{map_content}' with time taken to win level: {previous_time_to_win} minutes, hardness level: {hardness_level}, win/death ratio: {win_death_ratio}, predict a new map which should have the same structure as above but harder.\\n"
    "A: New map: [MAP]" where (len(TOKENS(MAP)) == 380) and STOPS_AT(MAP, '\\n')
    """


def generate_map(map_content, previous_time_to_win, hardness_level, win_death_ratio):
    response = generate_harder_map(
        map_content, previous_time_to_win, hardness_level, win_death_ratio
    )
    new_map_content = response.variables["MAP"]
    return Map(new_map_content)


map_content = [
    "BBBBBBBBBBBBBBBBBBBB",
    "B...E..............B",
    "B.......B..........B",
    "B....BBBB..........B",
    "B..................B",
    "B..................B",
    "B.........P........B",
    "B..................B",
    "B.............E....B",
    "B..................B",
    "B..................B",
    "B.........B........B",
    "B.........B........B",
    "B.........B........B",
    "BBBBBBBBBBBBBBBBBBBB",
]

previous_time_to_win = 5  # Dummy value in minutes
hardness_level = 40  # Dummy value from 1 to 100
win_death_ratio = 2.0  # Dummy value

new_map = generate_map(
    map_content, previous_time_to_win, hardness_level, win_death_ratio
)

print(new_map)
