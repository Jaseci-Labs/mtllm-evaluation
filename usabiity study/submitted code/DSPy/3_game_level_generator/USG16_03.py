import random

# Define the original map structure
original_map = [
    "B.B.B.B.B.",
    ".E...E....",
    ".E...E....",
    ".E...E....",
    ".....E....",
    ".E...E....",
    ".E...E....",
    "P........."
]

# Dummy parameters to simulate difficulty and adjustments
time_taken_to_win = 120  # Time taken to win level (in seconds)
hardness_level = 80  # Difficulty level (1-100)
win_death_ratio = 0.8  # Win/death ratio (higher means harder)

# Calculate adjustments based on parameters
increase_enemy_density = win_death_ratio > 0.5  # Increase enemy density if win/death ratio is high
increase_block_density = hardness_level > 50  # Increase block density if hardness level is high

# Function to generate a harder map based on adjustments
def generate_harder_map(original_map, increase_enemy_density, increase_block_density):
    new_map = []
    for row in original_map:
        new_row = list(row)  # Convert string row to list to modify characters
        for i in range(len(new_row)):
            if new_row[i] == ".":
                if increase_block_density and random.random() < 0.2:  # Increase block density randomly
                    new_row[i] = "B"
            elif new_row[i] == "E":
                if increase_enemy_density and random.random() < 0.3:  # Increase enemy density randomly
                    new_row[i] = "E"
        new_map.append("".join(new_row))  # Convert list back to string and append to new map
    return new_map

# Generate a new map with adjusted parameters
new_map = generate_harder_map(original_map, increase_enemy_density, increase_block_density)

# Output the new map
for row in new_map:
    print(row)
