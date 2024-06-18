import:py from jaclang.core.llms, Anthropic;


glob llm = Anthropic(model_name="claude-3-sonnet-20240229");

with entry{
    points:'prevous level points (0-10)':int = 3;

    map = [
        'BBBBBBBBBBBBBBBBBBBBBBBBB',
        'B..................E....B',
        'B.........P.............B',
        'B.....EEE.........EE....B',
        'BBBBBBBBBBBBBBBBBBBBBBBBB'
    ];

    can 'create a new list using the list given and make add more E letters in the middle of B letters if points are higher less E letters if points are lower create a new list using the list given and make add more E letters in the middle of B letters if points are higher less E letters if points are lower, B - Block or Obstacles, Enemies and the Player cannot pass through, . - Walkable are for all characters, E - Enemy Character, P - Player Character' newMap(oldMap:'old list': list[str], points:'previous level points':int) -> 'create a new list using the list given and make add more E letters in the middle of B letters if points are higher less E letters if points are lower': list[str] by llm();

    newList = newMap(map,points);

    print(newMap);    
}
