import:py from mtllm.llms.openai, OpenAICompletion;

glob llm = OpenAICompletion(model_name="gpt-3.5-turbo-instruct");

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
