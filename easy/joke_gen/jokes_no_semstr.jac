import:py from jaclang.core.llms, OpenAI;

glob llm = OpenAI(model_name="gpt-4o");

glob jokes: list[tuple[str, str]] = [
    ("How does a penguin build its house?", "Igloos it together."),
    ("Which knight invented King Arthur's Round Table?", "Sir Cumference.")
];

can tell_a_new_joke() -> tuple[str, str] by llm(incl_info=(jokes));

with entry {
    (joke, punchline) = tell_a_new_joke();
    print(f"{joke} : {punchline}");
}