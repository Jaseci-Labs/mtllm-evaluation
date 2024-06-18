import:py sys;
::py::
sys.path.append('/root/miniconda3/lib/python3.12/site-packages/Ollama')
::py::

import:py from jaclang.core.llms, Ollama;

glob llm = Ollama(
            model_name = "phi3:3.8b" # Will pull model if does not exists
            );

can 'evaluate essay'
evaluate(essay:str, evaluation_criteria:list)
    -> 'Grade out of 100 for evaluation_criteria and return A for score above 75 and B for score 65-75 and C for 55-65 and S for 35-55 and F for below 35 and provide evaluator remarks/reviews': str by llm(temperature=0.9, reason=True);
with entry {
    print(evaluate( 'The global power crisis is caused by high energy demand, old infrastructure, and reliance on fossil fuels. This crisis results in blackouts, higher costs for businesses, and problems for healthcare and education. To fix this, we need to use more renewable energy like solar and wind, update infrastructure, and use energy more efficiently. Better governance and regulations can help manage the crisis and attract investments for a stable energy future.', ["clarity", "coherance"]));
}

