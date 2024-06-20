import:py from jaclang.core.llms, Anthropic, Ollama, Groq;

glob llm = Groq();

obj Essay {
    has essay: 'Essay': str;

    can 'Evaluate the given essay based on the given criteria. Provide Detailed Judgement.'
    essay_judge(criteria: 'Criteria': str) -> 'Judgement': str by llm(incl_info=(self.essay));

    can 'Give essay a letter grade (A,B,C,D,S,F)'
    give_grade(summary: 'Summary': str) -> 'Grade': str by llm();
}

with entry{
    essay = """
The global power crisis is caused by high energy demand, old infrastructure, and reliance on fossil fuels. This crisis results in blackouts, higher costs for businesses, and problems for healthcare and education. To fix this, we need to use more renewable energy like solar and wind, update infrastructure, and use energy more efficiently. Better governance and regulations can help manage the crisis and attract investments for a stable energy future.
""";
    essay = Essay(essay);

    criterias = ["Clarity", "coherency", "relevance"];
    judgements = {};
    for criteria in criterias {
        judgement = essay.essay_judge(criteria);
        judgements[criteria] = judgement;
    }
    grade = essay.give_grade(summary);
    print("Evaluator's Remarks: ", summary);
    print("Grade: ", grade);
}