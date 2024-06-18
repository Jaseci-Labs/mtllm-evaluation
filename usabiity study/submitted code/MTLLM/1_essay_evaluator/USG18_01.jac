import:py from jaclang.core.llms, Anthropic;

glob llm = Anthropic(model_name="claude-3-sonnet-20240229");


obj Essay {
    has essay: 'Essay': str;

    can 'Provide a detailed judgement according to a given criterion'
    essay_judge(criterion: 'Criterion': str) -> 'Judgement': str by llm(incl_info=(self.essay));

    can 'Generate a summary based on judgements'
    generate_remarks(judgements: 'Judgements': dict) -> 'Summary': str by llm(incl_info=(self.essay));

    can 'Give essay a letter grade (A,B,C,S,F)'
    give_grade(remark: 'Remark': str) -> 'Grade': str by llm();
}

with entry{

    essay = """
    With a population of approximately 45 million Spaniards and 3.5 million immigrants,
    Spain is a country of contrasts where the richness of its culture blends it up with
    the variety of languages and dialects used. Being one of the largest economies worldwide,
    and the second largest country in Europe, Spain is a very appealing destination for tourists
    as well as for immigrants from around the globe. Almost all Spaniards are used to speaking at
    least two different languages, but protecting and preserving that right has not been
    easy for them. Spaniards have had to struggle with war, ignorance, criticism and the governments,
    in order to preserve and defend what identifies them, and deal with the consequences.
    """;

    essay = Essay(essay);

    criteria = ["Clarity", "Originality", "Evidence", "Coherence and Organization", "Grammar and Syntax", "Overall Impression"];
    judgements = {};
    for criterion in criteria {
        judgement = essay.essay_judge(criterion);
        judgements[criterion] = judgement;
    }
    remark = essay.generate_remarks(judgements);
    grade = essay.give_grade(remark);
    print("Reviewer Notes: ", remark);
    print("Grade: ", grade);
}

