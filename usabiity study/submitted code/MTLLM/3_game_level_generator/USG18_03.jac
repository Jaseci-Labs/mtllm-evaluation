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
    # Sample data from LMQL-based code
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

    # Create a GameLevel object
    game_level = GameLevel(map=previous_levels, time_taken=time_taken, win_death_ratio=win_death_ratio, hardness_level=hardness_level);

    # Generate a new level map
    new_level_map = game_level.generate_new_level();

    # Print the new level map
    for row in new_level_map{
        print(row);
    }
}
