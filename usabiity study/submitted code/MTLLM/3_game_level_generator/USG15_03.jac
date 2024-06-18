import:py from jaclang.core.llms, Ollama;
glob llm = Ollama(model_name="llama2:latest");

walker generate_harder_map {
    has map: list,
    previous_time_to_win:int,
    hardness_level:int,
    win_death_ratio:int,
    new_map:list;

    can generate_harder_map {
        prompt = """
        Given the previous level map:
        {map} of level 50,
        time taken to win level: {previous_time_to_win} minutes,
        hardness level: {hardness_level} in the range of 1-100,
        win/death ratio: {win_death_ratio},
        Predict a new map with structure built on as above but harder.
        The new map should only include the just map and no additional text, intro or explanation.

        Output can contain only following English characters! which have the following meaning
        "B" - Block or Obstacles, Enemies and the Player cannot pass through
        "." - Walkable area for all characters
        "E" - Enemy Character
        "P" - Player Character

        Each line of the map must contain 20! characters
        New map(each on a new line):
        """;

        response: llm.complete(prompt);
        new_map: response;
    }
}

walker main {
    has map: [
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
    ],
    previous_time_to_win: 5,  # Dummy value in minutes
    hardness_level: 40,  #/ Dummy value from 1 to 100
    win_death_ratio: 20;  # Dummy value

    generate_harder_map walker with {
        map: map,
        previous_time_to_win: previous_time_to_win,
        hardness_level: hardness_level,
        win_death_ratio: win_death_ratio
    };

    report generate_harder_map::new_map;
}
