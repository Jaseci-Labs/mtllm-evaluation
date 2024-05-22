import:py from jaclang.core.llms, BaseLLM;

obj model :BaseLLM: {
    can init(output_str: str) {
        self.output_str = output_str;
    }

    can __infer__(meaning_in: str, **kwargs: dict) {
        print(meaning_in);
        return f"[Output] {self.output_str}";
    }
}

glob llm = model(output_str="fromage");

glob examples: "Examples of English words translated to french" :dict[str,str] = {
    "sea otter": "loutre de mer",
    "peppermint": "menthe poivrée",
    "plush giraffe": "girafe en peluche"
};


can 'Translate English to French'
translate(english_word: 'English Word': str)-> 'French Word' :str by llm(incl_info=(examples));

with entry {
    print(translate("cheese"));
}