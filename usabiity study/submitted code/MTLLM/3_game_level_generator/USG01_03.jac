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

    
    
        can nextLevel -> 'Start the string with B and end with  B. Use only B,.,E,P characters such that length of a single string is 20 and there are 15 strings in the list and generate a harder levelmap/list. Output only the levelmap/list': list[str] by llm(incl_info=(self.levelmap), temperature=0.9);
    }

can 
findHardness(body : str)
    -> "B for obstacles,'.' for Walkable for all characters,'E' for Enemy characters,'P' for Player character. If the player needs to go to otherside, determine the hardness of the level in the body" : str by llm(temperature=0.8, reason=True);
can
findTime(body : str)
    -> "B for obstacles,'.' for Walkable for all characters,'E' for Enemy characters,'P' for Player character. If the player needs to go to otherside, estimatetime taken in minutes to complete the level in the body. Output only a number" : str by llm(temperature=0.8, reason=True);
#harder levelmap/list of strings with only B,.,E,P characters
with entry {
string = Game();
    next = string.nextLevel();
    print(next);
    print(findHardness(next));
    print(findTime(next));
}