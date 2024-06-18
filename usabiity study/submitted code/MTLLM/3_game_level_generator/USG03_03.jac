import:py sys;
::py::
sys.path.append('/root/miniconda3/lib/python3.12/site-packages/Ollama')
::py::

import:py from jaclang.core.llms, Ollama;

glob llm = Ollama(
    model_name = "phi3:3.8b"
);

obj "a list of strings of length 20 and with characters 'B','.','E','P'"
LevelMap {
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

    enum 'characters of the string'
    characters {
        B: 'Block or obstacles, enemies and the player cannot pass through',
        EQ: 'Walkable for all characters',
        E: 'Enemy characters',
        P: 'Player characters'
    }
        can generate_levelmap -> 'harder levelmap/list of strings with only B,.,E,P characters': list[str] by llm(incl_info=(self.levelmap), temperature=0.0);
    }


with entry {
    next_level = LevelMap();
    new_levelmap = next_level.generate_levelmap();
    print(new_levelmap);
}
