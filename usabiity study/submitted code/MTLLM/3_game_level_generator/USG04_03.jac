import:py from jaclang.core.llms, OpenAI;

glob llm = OpenAI(model_name="gpt-3.5-turbo");

obj Wall {
    has length: 'length of wall': int
}

obj Position {
    has x: 'distance from verticle axis at the center of map': int;
    has y: 'distance from horizontal axis at the center of map': int
}

obj Map {
    has level: 'Level of the map in this game': Level;
    has pos_obstacles: 'Obstacles in the map': list[Position];
    has pos_enemies: 'Enemies in the map': list[Position];
    has pos_player: 'Position of the player in map': Position;
    has walls: 'Walls in the map': list[Wall];
}

obj Level {
    has name: 'Number of the level': str;
    has hardness: 'Hardness of the level(0-100)': int;
    has no_wall: 'Number of walls': int;
    has no_enemies: 'Number of enemies': int;
    has duration: 'time taken to complete level': int;
}

obj generate_new_level_map{
    can (previous_map: Map) -> Map:
    prev_level = previous_map.level
    new_level_num = int(prev_level.name) + 1
    new_hardness = min(prev_level.hardness + 10, 100)
    new_no_wall = prev_level.no_wall + 1
    new_no_enemies = prev_level.no_enemies + 2
    new_duration = prev_level.duration + 5
    
    