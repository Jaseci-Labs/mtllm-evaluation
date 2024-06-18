import:py sys;
::py::
sys.path.append('/root/miniconda3/lib/python3.12/site-packages/Ollama')
::py::


import:py from jaclang.core.llms, Ollama;

glob language_model = Ollama(
            model_name = "phi3:3.8b" # Model will be pulled if it doesn't exist
            );

can 
evaluate_paragraph(paragraph: str, evaluation_criteria: str)
    -> 'complete the evaluation based on the criteria provided and explain the reasoning behind the grading' : str by language_model(temperature=0.8, reason=True);

glob criteria = "Evaluate based on clarity, grammar, organization and content. Grade the paragraph using A for the best, B for good, C for satisfactory, D for low pass, S for marginal failure, and F for failure.";
glob paragraph = """The global power crisis is caused by high energy demand, old infrastructure, and reliance on fossil fuels. This crisis results in blackouts, higher costs for businesses, and problems for healthcare and education. To fix this, we need to use more renewable energy like solar and wind, update infrastructure, and use energy more efficiently. Better governance and regulations can help manage the crisis and attract investments for a stable energy future.""";

with entry {
        print(evaluate_paragraph(paragraph, criteria));
}