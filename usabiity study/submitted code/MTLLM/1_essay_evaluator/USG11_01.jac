"import:py from jaclang.core.llms, Anthropic;

glob llm = Anthropic(model_name=""claude-3-sonnet-20240229"");


obj Essay {
    has essay: 'Essay': str;

    can 'Evaluate the given essay based on the given criteria. Provide Detailed Judgement.'
    essay_judge(criteria: 'Criteria': str) -> 'Judgement': str by llm(incl_info=(self.essay));

    can 'Generate a remark based on judgements'
    generate_remarks(judgements: 'Judgements': dict) -> 'Summary': str by llm(incl_info=(self.essay));

    can 'Give essay a letter grade (A,B,C,S,F)'
    give_grade(remark: 'Remark': str) -> 'Grade': str by llm();
}

with entry{

    essay = input(""Write your essay here : "");
    essay = Essay(essay);

    criterias = [""Clarity"",""Coherence"" , ""Originality"", ""Evidence"",""Correct Spelling and grammar""];
    judgements = {};
    for criteria in criterias {
        judgement = essay.essay_judge(criteria);
        judgements[criteria] = judgement;
    }
    remark = essay.generate_remarks(judgements);
    grade = essay.give_grade(remark);
    print("Reviewer Notes: ", remark);
    print("Grade: ", grade);
}