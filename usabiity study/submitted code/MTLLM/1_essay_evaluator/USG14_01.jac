"import:py from jaclang.core.llms, Anthropic;

glob llm = Anthropic(
            model_name = ""claude-3-sonnet-20240229""
            );

can 'Evaluate a given essay according to the given criteria and give a grade and reasons to give that grade' 
evaluate_essay(input:'Input essay': str, main_criteria: 'Main Criteria for evaluation': str) -> 'Evaluated grade chosen amoung A,B,C,D,S,F and the reasons to give that grade': str by llm();

with entry{
    essay = input(""Enter the essay to be evaluated: "");
    criteria = input(""Enter the main criteria for the evaluation: "");

    print(evaluate_essay(essay, criteria));
}"