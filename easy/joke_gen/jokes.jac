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

glob llm = model(output_str={"joke": "What kind of music do planets listen to?", "punchline": "Neptunes!"});

obj "A list of good dad jokes. A indicates the punchline"
JokeList {
    has jokes: 'Jokes with Punchlines' :list[dict] = [
        {
            "joke": "How does a penguin build its house?",
            "punchline": "Igloos it together."
        },
        {
            "joke": "Which knight invented King Arthur's Round Table?",
            "punchline": "Sir Cumference."
        }
    ];

    can 'Generate a Joke with Punchline'
    generate_joke_punchline() -> 'Joke with Punchline' :dict by llm(incl_info=(self.jokes));

    can generate {
        joke_punchline = self.generate_joke_punchline();
        self.jokes.append(joke_punchline);
    }
}
with entry{
    joker = JokeList();
    joker.generate();
    print(joker.jokes);
}