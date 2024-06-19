import:py dspy ;
import:py from dspy.teleprompt, BootstrapFewShot ;

with entry {
    llm = dspy.OpenAI(model="gpt-4o");    
    dspy.settings.configure(lm=llm);    

    examples: list[tuple[(list, str, str)]] = [
        (["skirt", "dress", "pen", "jacket"], "skirt is clothing, dress is clothing, pen is an object, jacket is clothing.", "pen"),
        (["Spain", "France", "German", "England", "Singapore"], "Spain, France, England, Singapore is a country, German is a language.", "German")
    ];    
    dataset = [dspy.Example(options=str(example[0]), reasoning=example[1], odd_word=example[2]).with_inputs("options") for example in examples];
}

"""Pict the Odd Word Out from the given list of words."""
class OddWordOut:dspy.Signature: {
    has options: str = dspy.InputField(desc="Options to pick from"),
        odd_word: str = dspy.OutputField(desc="Odd Word");
}

class OddWordOutModule:dspy.Module: {
    can init() {
        super.init() ;    
        self.generate_answer = dspy.ChainOfThought(OddWordOut);
    }
    
    can forward(options: str) {
        prediction = self.generate_answer(options=options);    
        return dspy.Prediction(odd_word=prediction.odd_word, rationale=prediction.rationale) ;
    }
}

with entry {
    get_odd_word_out = BootstrapFewShot().compile(OddWordOutModule(), trainset=dataset);    
    pred = get_odd_word_out("[Bentley, Ferrari, Lamborghini, Casio, Toyota]");    
    print((pred.rationale, pred.odd_word)) ;
}

