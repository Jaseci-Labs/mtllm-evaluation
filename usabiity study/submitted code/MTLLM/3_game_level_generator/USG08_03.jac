import:py from jaclang.core.llms, Ollama;

glob llm = Ollama(model_name="phi3");

obj MapNode {
    has char: 'Char': str;
    has next: 'Next': MapNode;
}

with entry {
    prev_level_map = "B..........E......P"
    time_taken = 60
    hardness = 80
    win_death_ratio = 2.5
    
    head = MapNode(char="", next=None);
    current_node = head;
    for char in prev_level_map {
        new_node = MapNode(char=char, next=None);
        current_node.next = new_node;
        current_node = new_node;
    }

    prompt = f"Previous Level Map: {prev_level_map}\nTime Taken: {time_taken}\nHardness: {hardness}\nWin/Death Ratio: {win_death_ratio}\nGenerate a new level map based on the previous level."
    current_node = head.next;
    while current_node is not None {
        prompt += current_node.char;
        current_node = current_node.next;
    }
    new_level_map = llm(prompt)
    
    print("New Level Map:")
    print(new_level_map)
}
