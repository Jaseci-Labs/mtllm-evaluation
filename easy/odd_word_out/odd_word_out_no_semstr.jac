import:py from mtllm.llms, OpenAI;

glob llm = OpenAI(model_name="gpt-4o");

glob examples: list[tuple[list[str], str, str]] = [
    (["skirt", "dress", "pen", "jacket"], "skirt is clothing, dress is clothing, pen is an object, jacket is clothing.", "pen"),
    (["Spain", "France", "German", "England", "Singapore"], "Spain, France, England, Singapore is a country, German is a language.", "German")
];

can odd_word_out(options: list[str]) -> tuple[str, str] by llm(incl_info=(examples));

with entry {
    print(odd_word_out(["Bentley", "Ferrari", "Lamborghini", "Casio", "Toyota"]));
}
