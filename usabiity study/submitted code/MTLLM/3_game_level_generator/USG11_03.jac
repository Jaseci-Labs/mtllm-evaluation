import:py from jaclang.core.llms, Anthropic;

glob llm = Anthropic(model_name="claude-3-sonnet-20240229");

obj GameLevel {
    has map: 'Map': list[str];
    has time_taken: 'Time Taken': int;
    has win_death_ratio: 'Win/Death Ratio': int;
    has hardness_level: 'Hardness Level': int;

    can 'Generate a level up map of the current level map'
    generate_new_level() -> 'New Map': list[str] by llm(incl_info=(self.map, self.time_taken, self.win_death_ratio, self.hardness_level));
}

with entry {
    # Example usage
    previous_level_map = [
        "BBBBBBBBBBBB",
        "B.........BB",
        "B..BBBBB...B",
        "B...PB.....B",
        "B..BE.E...BB",
        "B..........B",
        "BBBBBBBBBBBB"
    ];

    time_taken = 120;  # in seconds
    win_death_ratio = 3;  # 3 wins for every 1 death
    hardness_level = 70;  # on a scale of 1 to 100

    # Create a GameLevel object
    game_level = GameLevel(map=previous_level_map, time_taken=time_taken, win_death_ratio=win_death_ratio, hardness_level=hardness_level);

    # Generate a new level map
    new_level_map = game_level.generate_new_level();

    # Print the new level map
    for row in new_level_map{
        print(row);
    }
        
}
