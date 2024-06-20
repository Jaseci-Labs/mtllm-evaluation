import:py sys;
::py::
sys.path.append('/root/miniconda3/lib/python3.12/site-packages/Ollama')
::py::

import:py from jaclang.core.llms, Ollama;

glob llm = Ollama(
    model_name = "phi3:3.8b"
);

obj
Game {
    has levelmap: "list of strings of length 20 with only 'B','.','E','P' characters": list[str] = [
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
    has time_taken: int = 10;  // Dummy value for time taken to win level
    has hardness_level: int = 50;  // Dummy value for hardness level (1-100)
    has win_death_ratio: float = 1.5;  // Dummy value for win/death ratio

    can nextLevel -> 'Generate a harder level map based on previous level map, time taken, hardness level, and win/death ratio. Start each string with B and end with B. Use only B,.,E,P characters. Output only the new level map': list[str] by llm(incl_info=(self.levelmap, self.time_taken, self.hardness_level, self.win_death_ratio), temperature=0.9);
}

can 
findHardness(body: str) 
    -> "Determine the hardness of the level. B for obstacles,'.' for walkable areas,'E' for enemy characters,'P' for player character. Output a hardness level from 1-100": str by llm(temperature=0.8, reason=True);

can 
findTime(body: str) 
    -> "Estimate time taken in minutes to complete the level. B for obstacles,'.' for walkable areas,'E' for enemy characters,'P' for player character. Output only a number": str by llm(temperature=0.8, reason=True);

with entry {
    level = Game();
    next_level = level.nextLevel();
    print(next_level);
    hardness = findHardness(next_level);
    print(hardness);
    time_to_complete = findTime(next_level);
    print(time_to_complete);
}
