import:py from jaclang.core.llms, Anthropic;

 glob llm = Anthropic(model_name="claude-3-sonnet-20240229");


obj Essay {
    has essay: 'Essay': str;

    can 'Evaluate the given essay based on the given criteria. Provide Detailed Judgement.'
    essay_judge(criteria: 'Criteria': str) -> 'Judgement': str by llm(incl_info=(self.essay));

    can 'Generate a Review'
    generate_review(judgements: 'Judgements': dict) -> 'review': str by llm(incl_info=(self.essay));

    can 'Give essay a letter grade (A, B, C, S, F)'
    give_grade(review: 'Review': str) -> 'Grade': str by llm();
}

with entry{
    essay = input("Give your Essay : ");

    essay = Essay(essay);

    criterias = ["Clarity","Persuasiveness", "Originality","Creativity", "Evidence","Grammar and Syntax","Conclusion"];
    judgements = {};
    for criteria in criterias {
        judgement = essay.essay_judge(criteria);
        judgements[criteria] = judgement;
    }
    review = essay.generate_review(judgements);
    grade = essay.give_grade(review);
    print("Reviewer Notes: ", review);
    print("Grade: ", grade);
}