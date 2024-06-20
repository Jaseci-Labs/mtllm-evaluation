"""
This module demonstrates generating a harder map based on the previous level map, time taken to win level, hardness level, and win/death ratio.
"""

import:py random;

# Map Description
glob MAP_WIDTH = 18;
glob MAP_HEIGHT = 15;
glob PREVIOUS_MAP = [
  "BBBBBBBBBBBBBBBB",
    "B...E............B",
    "B........B........B",
    "B....BBBB........B",
    "B................B",
    "B...............B",
    "B................B",
    "B.............P..B",
    "B................B",
    "B..............E..B",
    "B................B",
    "B...............B",
    "B........B........B",
    "B.........B.......B",
    "B.........B......B",
    "BBBBBBBBBBBBBBBBBB''
];

# Parameters for map generation
glob WIN_TIME_PREV = 300;  # in seconds
glob HARDNESS_LEVEL_PREV = 50;  # scale from 1 to 100
glob WIN_DEATH_RATIO_PREV = 3;  # number of wins per death

# Harder map parameters
glob HARDNESS_MULTIPLIER = 1.2;  # increase difficulty by 20%

# Function to generate a harder map
can generate_harder_map() -> list[str] {
    new_map = PREVIOUS_MAP[:];
    hardness_factor = HARDNESS_LEVEL_PREV * HARDNESS_MULTIPLIER;

    for y in range(1, MAP_HEIGHT - 1) {
        for x in range(1, MAP_WIDTH - 1) {
            if new_map[y][x] == '.' and random.random() < (hardness_factor / 100):
                new_map[y] = new_map[y][:x] + 'E' + new_map[y][x+1:];

    return new_map;
}

with entry {
    harder_map = generate_harder_map();
    print("Harder Map:");
    for row in harder_map:
        print(row);
}
