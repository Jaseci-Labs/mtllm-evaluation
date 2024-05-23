import:py from jaclang.core.llms, Anthropic;

glob llm = Anthropic();

glob examples: "Example Translations" :dict[str,str] = {
    "sea otter": "loutre de mer",
    "peppermint": "menthe poivrée",
    "plush giraffe": "girafe en peluche"
};

can 'Translate'
translate(english_word: 'English Word': str)-> 'Translation' :str by llm(incl_info=(examples));

with entry {
    print(translate("cheese"));
}