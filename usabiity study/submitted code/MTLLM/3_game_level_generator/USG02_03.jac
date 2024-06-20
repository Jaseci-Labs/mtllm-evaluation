global llm = OpenAI();

walker game_level_generator {
    has previous_map, time_taken, hardness_level, win_death_ratio;

    can generate_harder_map {
        report {
            prompt = f
            """
            Previous Level Map: 
            {previous_map}
            Time Taken: {time_taken} seconds
            Hardness Level: {hardness_level}
            Win/Death Ratio: {win_death_ratio}

            Generate a new level map with the same structure as the previous map, but harder
            """
            harder_map = llm.prompt(prompt)
            harder_map
        }
    }
}

walker init {
    spawn here > game_level_generator {
        previous_map: """
        P...B
        ..B..
        ...E.
        E..B.
        .B...
        """,
        time_taken: 120,  # in seconds
        hardness_level: 50,  # on a scale of 1-100
        win_death_ratio: 2.0  # wins per death
    };
    take > game_level_generator.generate_harder_map;
    print(take)
}
