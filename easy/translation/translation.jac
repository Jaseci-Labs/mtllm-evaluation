import:py from mtllm.llms, Ollama;

glob llm = Ollama(host="http://52.23.242.52:11343");

glob examples: "Example Translations": dict[str, str] = {
    "sea otter": "loutre de mer",
    "peppermint": "menthe poivrée",
    "plush giraffe": "girafe en peluche"
};

can 'Translate'
translate(english_word: 'English Word': str) -> 'Translation': str by llm(incl_info=(examples));

with entry {
    print(translate("cheese"));
}
