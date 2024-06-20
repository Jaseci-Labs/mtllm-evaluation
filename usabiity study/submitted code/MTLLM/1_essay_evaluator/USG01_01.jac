# import:py sys;
# ::py::
# sys.path.append('/root/miniconda3/lib/python3.12/site-packages/Ollama')
# ::py::

import:py from jaclang.core.llms, OpenAI;

glob llm = OpenAI(model_name='gpt-4o');
can 
summarize(body : str, criteria : str)
    -> 'complete the task described in the above criteria and give resoning for your answer' : str by llm(temperature=0.8, reason=True);

glob cri = "Evaluate based on clarity,Grammar, Sentence structure, Organization and content. Grade the sentence using A for the best, B for the good, C for the Satisfactory, D for the Low Pass, but certifying, S for the Low Failure and F for the Failure. ";
glob para = """The global power crisis is caused by high energy demand, old infrastructure, 
    and reliance on fossil fuels. This crisis results in blackouts, higher costs 
    for businesses, and problems for healthcare and education. To fix this, we need 
    to use more renewable energy like solar and wind, update infrastructure, and use 
    energy more efficiently. Better governance and regulations can help manage the crisis 
    and attract investments for a stable energy future.""";

with entry {
        print(summarize(para, cri));
}