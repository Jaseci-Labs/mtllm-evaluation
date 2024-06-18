import:py from jaclang.core.llms, Anthropic;

glob llm = Anthropic(model_name="claude-3-sonnet-20240229");

glob context:str =  "# These rules must be strictly adhered to while creating a maps."
                    "- Must have only single Player (P) in map at the middle of the map ."
                    "- Two consecutive maps should not look alike."
                    "- Hardness should be slightly increased between consecutive maps."
                    "- All enemies should be accessible to the player (should not be enclosed with blocks)."
                    "- Hardnes of a level can be determined by the time taken to complete a level and number of retry attempts.";

obj 'Consists of the level configuration data of a certain level'
Map {
    has Level_no:int = 1;
    has time_to_win_level:'in seconds':float = 60.0;
    has nos_retry:'How many retry attempts before completing the level':int = 0;
    has map:
    'the map of the level having (B) as block, (E) as enemy, (P) as player and (.) as empty space. All outer characters are B. Only one single player character (P) can be in the map. horizontal 20 characters and vertical 15 items'
    :list[str] = [
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

                            ];
}

with entry {
    map = Map(by llm(incl_info=(context)));
    for line in map.map{
        print(line);
    }
        
}

