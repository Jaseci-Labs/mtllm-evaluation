import:py from mtllm.llms, Ollama;

glob llm = Ollama(host="http://52.23.242.52:11343");

glob jokes: 'Jokes with Punchlines': list[tuple[str, str]] = [
    ("How does a penguin build its house?", "Igloos it together."),
    ("Which knight invented King Arthur's Round Table?", "Sir Cumference.")
];

can 'Generate a new Joke with Punchline'
tell_a_joke() -> 'Joke with Punchline': tuple[str, str] by llm(incl_info=(jokes));

with entry {
    (joke, punchline) = tell_a_joke();
    print(f"{joke} : {punchline}");
}
