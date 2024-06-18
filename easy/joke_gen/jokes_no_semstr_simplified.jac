import:py from jaclang.core.llms, OpenAI;

glob llm = OpenAI(model_name="gpt-4o");

can generate_joke_n_punchline() -> tuple[str, str] by llm();

with entry {
    (joke, punchline) = generate_joke_n_punchline();
    print(f"{joke} : {punchline}");
}