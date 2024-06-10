import:py from mtllm.llms, Ollama;

glob llm = Ollama(verbose=True, host="http://52.23.242.52:11343");

glob examples: 'Examples for Picking Odd Word out (Options, Reasoing, Result)': list[tuple[list[str], str, str]] = [
    (["skirt", "dress", "pen", "jacket"], "skirt is clothing, dress is clothing, pen is an object, jacket is clothing.", "pen"),
    (["Spain", "France", "German", "England", "Singapore"], "Spain, France, England, Singapore is a country, German is a language.", "German")
];

can 'Pick the Odd word out'
odd_word_out(options: 'Options to pick from': list[str]) -> 'Odd Word': str by llm(incl_info=(examples), method="Reason");

with entry {
    print(odd_word_out(["Bentley", "Ferrari", "Lamborghini", "Casio", "Toyota"]));
}
