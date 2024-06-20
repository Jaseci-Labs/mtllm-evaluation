import lmql

# Initialize LMQL engine
lmql_engine = lmql.Engine()


# Function to analyze previous level maps
def analyze_previous_levels(previous_maps, time_taken, win_death_ratio, hardness_level):
    # Analyze previous level maps and player performance metrics using LMQL
    insights = {}

    # Analyze structure and characteristics of previous level maps
    map_analysis_query = "Analyze structure and characteristics of previous level maps: [MAP_ANALYSIS] based on pervious_map"
    response = lmql_engine.query(map_analysis_query)
    insights["map_analysis"] = response["MAP_ANALYSIS"]

    # Analyze player performance metrics (time taken, win/death ratio, hardness level)
    player_performance_query = "Analyze other metrics: [METRICS] based on time_taken,win_death_ratio,hardness_level"
    response = lmql_engine.query(player_performance_query)
    insights["metrics"] = response["METRICS"]

    return insights


# Function to generate a new level map
def generate_new_map(insights):
    # Generate a new level map based on insights from previous levels using LMQL
    new_map_query = f"""
    Generate a new level map based on insights from previous levels:
    - Previous level map analysis: {insights['map_analysis']}
    - Other metrics time_taken,win_death_ratio,hardness_level : {insights['metrics']}
    [NEW_MAP]
    """
    response = lmql_engine.query(new_map_query)
    new_map = response["NEW_MAP"]

    return new_map


# Main function to execute the task
def main():
    # Example of previous level maps (dummy data)
    previous_level_map = [
        "BBBBBBBBBBBB",
        "B.........BB",
        "B..BBBBB...B",
        "B...PB.....B",
        "B..BE.E...BB",
        "B..........B",
        "BBBBBBBBBBBB",
    ]
    time_taken = 120
    win_death_ratio = 3
    hardness_level = 70

    # Analyze previous level maps and player performance
    insights = analyze_previous_levels(
        previous_level_map, time_taken, win_death_ratio, hardness_level
    )

    # Generate a new level map based on insights
    new_map = generate_new_map(insights)

    # Display the new level map
    print("New Level Map:")
    print(new_map)


if __name__ == "__main__":
    main()
