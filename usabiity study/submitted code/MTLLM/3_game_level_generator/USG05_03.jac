import:py from jaclang.core.llms, Anthropic;

glob llm = Anthropic(model_name="claude-3-sonnet-20240229");



# Current Map
glob map: '"B"-Block or Obstacles, Enemies and the Player cannot pass through, "."-Walkable area for all characters, "E"-Enemy Character(can have many), "P"-Player Character.There should be only one player' :list = [
"BBBBBBBBBBBBBBBBBBBBB",
"B.............E....B",
"B...........B......B",
"B........BBBB......B",
"B..................B",
"B..................B",
"B..................B",
"B.......P..........B",
"B..................B",
"B..........E.......B",
"B..................B",
"B..................B",
"B..................B",
"B.....B............B",
"B.....B............B",
"BBBBBBBBBBBBBBBBBBBBB"
];


# Next level map generating method
can 'Generate the next map based on the parameters. Next map should have the same structure as current map but harder.'
generate_next_map(current_map: 'This is the current Map' : list, 
                  other_parameters: 'This is the player parameters': dict) -> 'next_map' : list by llm();


with entry {
    # Dummy parameters
    parameters = {
        "time taken to win curent level": "2 minutes",
        "hardness level (1-100)": 40,
        "win/death ratio": "5/3"
    };

    next_map = generate_next_map(map, parameters);


    # Printing the next level map
    for i=0 to i<len(next_map) by i+=1 {
        print(next_map[i]);
    }


}