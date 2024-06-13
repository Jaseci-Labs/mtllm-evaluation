import:py from jaclang.core.llms, OpenAI;

glob llm = OpenAI(model_name="gpt-4o");

obj Essay {
    has essay: 'Essay': str;

    can 'Evaluate the given essay based on the given criteria. Provide Detailed Judgement.'
    essay_judge(criteria: 'Criteria': str) -> 'Judgement': str by llm(incl_info=(self.essay));
    can 'Generate a summary with the given judgements.'
    generate_summary(judgements: 'Judgements': dict) -> 'Summary': str by llm(incl_info=(self.essay));
    can 'Give essay a letter grade (A-D)'
    give_grade(summary: 'Summary': str) -> 'Grade': str by llm();
}

with entry {
    essay = "Sigiriya is an ancient rock fortress located in central Sri Lanka. Rising up 660 feet (200 meters) from the surrounding plains, the massive rock column was transformed into an impregnable palace-fortress in the late 5th century AD by King Kasyapa. The site contains the ruins of elaborate gardens, fountains, frescoes of maidens that once adorned the rock face, and a gateway in the form of an enormous lion. Declared a UNESCO World Heritage Site in 1982, Sigiriya is considered one of the best preserved examples of ancient urban planning and is one of Sri Lanka's major attractions for visitors due to its archaeological significance and striking aesthetic beauty.";
    essay = Essay(essay);
    criterias = ["Clarity", "Originality", "Evidence"];
    judgements = {};
    for criteria in criterias {
        judgement = essay.essay_judge(criteria);
        judgements[criteria] = judgement;
    }
    summary = essay.generate_summary(judgements);
    grade = essay.give_grade(summary);
    print("Reviewer Notes: ", summary);
    print("Grade: ", grade);
}
