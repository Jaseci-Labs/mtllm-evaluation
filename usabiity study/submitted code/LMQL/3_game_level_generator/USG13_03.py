import lmql

query_code = """
lmql
"""
### Define the prompt template
prompt_template = """
Given the current map:
{current_map}

and the parameters:
{other_parameters}

Generate the next map. The next map should have the same structure as the current map but be harder. "B" represents blocks or obstacles, which enemies and the player cannot pass through. "." represents walkable areas for all characters. "E" represents enemy characters (there can be many), and "P" represents the player character (there should be only one player). Provide the map only.
"""


def generate_next_map(current_map, parameters):
    prompt = prompt_template.format(
        current_map=current_map, other_parameters=parameters
    )

    query = f"""
    argmax
    "api:anthropic",
    model="gpt-4",
    api_key=claude_api_key,
    prompt={prompt},
    temperature=0.7,
    max_tokens=1000
    end

    next_map
    """

    result = lmql.query(query)

    return result[0]["next_map"]


map_data = """
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

parameters_data = """
    time taken to win current level: 2 minutes,
    hardness level (1-100): 40,
    win/death ratio: 5/3
"""

next_map_result = generate_next_map(map_data, parameters_data)

print(next_map_result)
