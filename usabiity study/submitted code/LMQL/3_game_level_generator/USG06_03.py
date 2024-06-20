
original_map = [
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
];


time_taken_to_win = 300  
hardness_level = 50  
win_death_ratio = 2.5  

f"""
Based on the following criteria, generate a new level map that is harder:
1. The previous level map,
2. Time taken to win level: {time_taken_to_win} seconds,
3. Hardness level: {hardness_level} (1-100),
4. Win/death ratio: {win_death_ratio}.

Original level map:
{'\\n'.join(original_map)}

New harder level map:
"""

lmql_query = f"""
    generate {
        for i in range(15):
            line = []
            for j in range(20):
                if j == 0 or j == 19 or i == 0 or i == 14:
                    line.append("B")
                else:
                    character = ["B", ".", "E", "P"]
                    if character == "P":
                        if any("P" in previous_line for previous_line in previous_lines):
                            character = "."
                    line.append(choice(character))
            previous_lines.append("".join(line))
            print(previous_lines[-1])
    }
"""


