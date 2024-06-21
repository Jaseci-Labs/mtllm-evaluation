import:py from mtllm.llms, OpenAI;

glob llm = OpenAI(model_name="gpt-4o");

glob examples: dict[str, str] = {
    "sea otter": "loutre de mer",
    "peppermint": "menthe poivrée",
    "plush giraffe": "girafe en peluche"
};

can translate(english_word: str) -> str by llm(incl_info=(examples));

with entry {
    print(translate("cheese"));
}
