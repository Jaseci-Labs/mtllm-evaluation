import numpy as np


def generate_harder_map(previous_map, time_taken, hardness_level, win_death_ratio):
    # Dummy strategy: Increase number of obstacles and enemies

    # Dimensions of the previous map
    rows, cols = len(previous_map), len(previous_map[0])

    # Initialize new map with same structure as previous map
    new_map = np.copy(previous_map)

    # Example strategies (can be adjusted based on real metrics)
    obstacle_increase = int(
        hardness_level / 10
    )  # Increase obstacles based on hardness level
    enemy_density = int(
        win_death_ratio * 10
    )  # Increase enemy density based on win/death ratio

    # Example: Increase number of obstacles
    for i in range(rows):
        for j in range(cols):
            if previous_map[i][j] == "B":
                # Increase number of blocks
                new_map[i][j] = "B"
                for _ in range(obstacle_increase):
                    # Introduce more obstacles in adjacent cells (if within bounds)
                    adj_i = i + np.random.randint(-1, 2)
                    adj_j = j + np.random.randint(-1, 2)
                    if (
                        0 <= adj_i < rows
                        and 0 <= adj_j < cols
                        and new_map[adj_i][adj_j] == "."
                    ):
                        new_map[adj_i][adj_j] = "B"

            elif previous_map[i][j] == "E":
                # Increase number of enemies
                new_map[i][j] = "E"
                for _ in range(enemy_density):
                    # Introduce more enemies in adjacent cells (if within bounds)
                    adj_i = i + np.random.randint(-1, 2)
                    adj_j = j + np.random.randint(-1, 2)
                    if (
                        0 <= adj_i < rows
                        and 0 <= adj_j < cols
                        and new_map[adj_i][adj_j] == "."
                    ):
                        new_map[adj_i][adj_j] = "E"

    return new_map


# Example usage
previous_level_map = [
    [".", ".", ".", ".", "."],
    [".", "B", ".", ".", "."],
    [".", ".", "E", ".", "."],
    [".", ".", ".", "P", "."],
]

time_taken_to_win = 120  # in seconds
hardness = 80  # on a scale of 1-100
win_death_ratio = 3.5  # example win/death ratio

new_map = generate_harder_map(
    previous_level_map, time_taken_to_win, hardness, win_death_ratio
)

# Print the new map
for row in new_map:
    print(" ".join(row))
