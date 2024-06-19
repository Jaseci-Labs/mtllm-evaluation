import:py from jaclang.core.llms, OpenAI;

glob llm = OpenAI(model_name="gpt-4o");

can joke_punchline() -> tuple[str, str] by llm();

with entry {
    (joke, punchline) = joke_punchline();
    print(f"{joke} : {punchline}");
}