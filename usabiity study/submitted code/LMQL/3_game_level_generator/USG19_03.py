# Define input variables
var previous_map = [
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
    "BBBBBBBBBBBBBBBBBB"
]

var time_taken_to_win = 300  # Time in seconds
var hardness_level = 50      # Hardness level (1-100)
var win_death_ratio = 0.5    # Win/death ratio

# Function to generate a new map
function generate_harder_map(previous_map, time_taken_to_win, hardness_level, win_death_ratio) {
    # Initialize a new map with the same structure as the previous map
    var new_map = []
    
    for row in previous_map {
        new_row = ""
        for char in row {
            if char == 'B' {
                new_row += 'B'  # Keep obstacles in the same place
            } else if char == '.' {
                new_row += '.'  # Keep walkable area
            } else if char == 'E' {
                new_row += 'E'  # Keep enemy positions
            } else if char == 'P' {
                new_row += 'P'  # Keep player position
            }
        }
        new_map.append(new_row)
    }
    
    # Increase difficulty by adding more enemies or obstacles
    for i in range(0, len(new_map)):
        for j in range(0, len(new_map[i])):
            if new_map[i][j] == '.' and rand(0, 100) < hardness_level:
                new_map[i] = new_map[i][:j] + 'E' + new_map[i][j+1:]
    
    return new_map
}

# Generate a harder map
var harder_map = generate_harder_map(previous_map, time_taken_to_win, hardness_level, win_death_ratio)

# Output the new, harder map
query {
    f"New Harder Map:\n{harder_map}"
}
