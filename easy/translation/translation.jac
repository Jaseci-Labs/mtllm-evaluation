import:py from jaclang.core.llms, OpenAI;

glob llm = OpenAI(model_name="gpt-4o");

glob examples: "Example Translations": dict[str, str] = {
    "sea otter": "loutre de mer",
    "peppermint": "menthe poivrée",
    "plush giraffe": "girafe en peluche"
};

can 'Translate'
translate(english_word: 'English Word': str) -> 'Translation': str by llm(incl_info=(examples));

with entry {
    print(translate("chair"));
}
