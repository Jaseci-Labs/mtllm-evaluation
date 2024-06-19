import:py dspy ;
import:py from dspy.teleprompt, BootstrapFewShot ;

with entry {
    llm = dspy.OpenAI(model="gpt-4o");    
    dspy.settings.configure(lm=llm) ;    
    examples: dict[(str, str)] = {
        "sea otter": "loutre de mer",
        "peppermint": "menthe poivrée",
        "plush giraffe": "girafe en peluche"
    };    
    dataset = [dspy.Example(
        english_word=english_word,
        translation=translation
    ).with_inputs(
        "english_word"
    ) for (english_word, translation) in examples.items()];
}

"""Translate the given English word"""
class Translation : dspy.Signature : {
    with entry {
        english_word: str = dspy.InputField(desc="English word to translate");    
        translation: str = dspy.OutputField(desc="Translation");
    }
}

class TranslationModule : dspy.Module : {
    can init() {
        super.init() ;    
        self.generate_answer = dspy.Predict(Translation);
    }
    
    can forward(english_word: str) {
        prediction = self.generate_answer(english_word=english_word);    
        return dspy.Prediction(translation=prediction.translation) ;
    }
}

with entry {
    translate = BootstrapFewShot().compile(
        TranslationModule(),
        trainset=dataset
    );    
    pred = translate(english_word="cheese");    
    print(pred.translation) ;
}

