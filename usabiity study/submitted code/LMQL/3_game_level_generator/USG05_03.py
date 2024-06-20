import lmql

# Define the prompt template
prompt_template = '''
Generate the next map based on the parameters. 
Next map should have the same structure as the current map but harder. 
"B"-Block or Obstacles, Enemies and the Player cannot pass through, 
"."-Walkable area for all characters, 
"E"-Enemy Character(can have many), 
"P"-Player Character.There should be only one player

Current Map:
{current_map}

Parameters:
Time taken to win current level: {time_taken},
Hardness level (1-100): {hardness_level},
Win/death ratio: {win_death_ratio}

Next Map:
'''

# Define the LMQL query
query = '''
lmql.query("""
    {prompt}
""",
variables={
    "prompt": prompt_template.format(
        current_map=current_map,
        time_taken=parameters["time_taken"],
        hardness_level=parameters["hardness_level"],
        win_death_ratio=parameters["win_death_ratio"]
    )
})
'''

# Current Map
current_map = '''
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
'''

# Parameters
parameters = {
    "time_taken": "2 minutes",
    "hardness_level": 40,
    "win_death_ratio": "5/3"
}

# Generate the next map
result = lmql.run(query)

# Extract and print the next map
next_map = result['next_map']
for line in next_map:
    print(line)
