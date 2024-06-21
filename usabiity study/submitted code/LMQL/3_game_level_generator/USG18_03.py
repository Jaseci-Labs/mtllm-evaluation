import lmql

lmql_engine = lmql.Engine()


def analyze_previous_levels(
    previous_levels, time_taken, win_death_ratio, hardness_level
):
    insights = {}

    map_analysis_query = f"""
    Analyze structure and characteristics of previous level maps:
    - Previous Levels: {previous_levels}
    [MAP_ANALYSIS]
    """
    response = lmql_engine.query(map_analysis_query)
    insights["map_analysis"] = response["MAP_ANALYSIS"]

    player_performance_query = f"""
    Analyze player performance metrics:
    - Time Taken: {time_taken} seconds
    - Win/Death Ratio: {win_death_ratio}
    - Hardness Level: {hardness_level}%
    [METRICS]
    """
    response = lmql_engine.query(player_performance_query)
    insights["metrics"] = response["METRICS"]

    return insights


def generate_new_map(insights):
    new_map_query = f"""
    Generate a new level map based on insights from previous levels:
    - Previous level map analysis: {insights['map_analysis']}
    - Player performance metrics: {insights['metrics']}
    [NEW_MAP]
    """
    response = lmql_engine.query(new_map_query)
    new_map = response["NEW_MAP"]

    return new_map


def main():
    previous_levels = [
        "WWWWWWWWWWWW",
        "W.........WW",
        "W..WWWWWW..W",
        "W..........W",
        "W..W....W..W",
        "W..........W",
        "WWWWWWWWWWWW",
    ]
    time_taken = 180
    win_death_ratio = 5
    hardness_level = 90

    # Analyze previous levels and player performance
    insights = analyze_previous_levels(
        previous_levels, time_taken, win_death_ratio, hardness_level
    )

    # Generate a new level map based on insights
    new_map = generate_new_map(insights)

    # Display the new level map
    print("New Level Map:")
    print(new_map)


if __name__ == "__main__":
    main()
