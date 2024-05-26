import:py from jaclang.core.llms, OpenAI;

glob llm = OpenAI(model_name="gpt-4o");

glob jokes: 'Jokes with Punchlines': list[tuple[str, str]] = [
    ("How does a penguin build its house?", "Igloos it together."),
    ("Which knight invented King Arthur's Round Table?", "Sir Cumference.")
];

can 'Generate a new Joke with Punchline'
tell_a_joke() -> 'Joke with Punchline': tuple[str, str] by llm(incl_info=(jokes));

with entry:__main__ {
    (joke, punchline) = tell_a_joke();
    print(f"{joke} : {punchline}");
}
