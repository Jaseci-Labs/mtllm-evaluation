import:py from jaclang.core.llms, Anthropic;

glob llm = Anthropic(model_name="claude-3-sonnet-20240229");

obj GameLevelGenerator {
    has map: list[str];
    has time_taken: int;
    has win_death_ratio: float;
    has hardness_level: int;

     can 'Generate a new level map based on previous playthroughs.Map should have only B(for blocks), E(for enemies), P(for player and only one P should be there) and .(for walkable).It should not include spaces(" ") It should have only 144 elements .'
    generate_level() -> list[str] by llm(incl_info=(self.map, self.time_taken, self.win_death_ratio, self.hardness_level));
}

with entry {
    # Example previous level map
    previous_map = [
        "BBBBBBBBBBBB",
        "B.........BB",
        "B..BBBBB...B",
        "B...PB.....B",
        "B..BE.E...BB",
        "B..........B",
        "BBBBBBBBBBBB"
    ];
    
    # Dummy values for time taken, hardness level, and win/death ratio
    time_taken = 60 ; # in seconds
    hardness_level = 80  ;# on a scale of 1-100
    win_death_ratio = 2.5 ; # for example, 2.5 wins per death
    
    generator = GameLevelGenerator(
        map=previous_map, 
        time_taken=time_taken, 
        win_death_ratio=win_death_ratio, 
        hardness_level=hardness_level
    );
    
     


    new_map = generator.generate_level();
    
    for elements in new_map {
       print(elements);
   }
}
