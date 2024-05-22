import:py from jaclang.core.llms, BaseLLM;

obj model :BaseLLM: {
    can init(output_str: str) {
        self.output_str = output_str;
    }

    can __infer__(meaning_in: str, **kwargs: dict) {
        print(meaning_in);
        return f"[Output] {self.output_str}";
    }
}

glob llm = model(output_str='Singer(name="Bruno Mars", age=38, top_songs=["Just the Way You Are", "Grenade"])');
obj 'Singer'
Singer {
    has name: 'Name of the Singer' :str,
        age: 'Age' :int,
        top_songs: "His/Her's Top 2 Songs": list[str];
}

with entry{
    bruno_mars = Singer(name="Bruno Mars" by llm());
    print(f"{bruno_mars.name} is {bruno_mars.age} years old. His top 2 songs are {bruno_mars.top_songs}.");
}
