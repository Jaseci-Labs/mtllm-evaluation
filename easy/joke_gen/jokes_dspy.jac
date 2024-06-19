import:py dspy ;
import:py from dspy.teleprompt, BootstrapFewShot ;

with entry {
    llm = dspy.OpenAI(model="gpt-4o");    
    dspy.settings.configure(lm=llm) ;    
    examples: list[tuple[(str, str)]] = [
        ("How does a penguin build its house?", "Igloos it together."),
        ("Which knight invented King Arthur's Round Table?", "Sir Cumference.")
    ];    
    dataset = [dspy.Example(joke=example[0], punchline=example[1]).with_inputs() for example in examples];
}

"""Tell a joke with a punchline."""
class JokeWithPunchline : dspy.Signature : {
    with entry {
        joke: str = dspy.OutputField(desc="Joke");    
        punchline: str = dspy.OutputField(desc="Punchline");
    }
}

class JokeWithPunchlineModule : dspy.Module : {
    can init() {
        super.init() ;    
        self.generate_answer = dspy.Predict(JokeWithPunchline);
    }
    
    can forward() {
        pred = self.generate_answer();    
        return dspy.Prediction(joke=pred.joke, punchline=pred.punchline) ;
    }
}

with entry {
    tell_a_joke = BootstrapFewShot().compile(
        JokeWithPunchlineModule(),
        trainset=dataset
    );    
    pred = tell_a_joke();    
    print(f"{pred.joke}{": "}{pred.punchline}") ;
}

