import:py from jaclang.core.llms, OpenAI;

glob llm = OpenAI(model_name="gpt-4o");

obj 'Singer'
Singer {
    has name: 'Name of the Singer': str,
        age: 'Age': int,
        top_songs: "His/Her's Top 2 Songs": list[str];
}

with entry {
    bruno_mars = Singer(name="Ed Sheeran" by llm());
    print(
        f"{bruno_mars.name} is {bruno_mars.age} years old. His top 2 songs are {bruno_mars.top_songs}."
    );
}
