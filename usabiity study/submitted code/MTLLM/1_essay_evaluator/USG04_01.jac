
import:py from jaclang.core.llms, OpenAI;

glob llm = OpenAI(model_name="gpt-3.5-turbo");

obj EssayObj {
    has essay: 'EssayObj': str;

    can 'Evaluate the given essay based on the given criteria and give judgement.'
    essay_eval(criterion: 'Criterion': str) -> 'Judgement': str by llm(incl_info=(self.essay));
    can 'Give evaluator's remarks with the given judgements.'
    generate_review(judgements: 'Judgements': dict) -> 'Review': str by llm(incl_info=(self.essay));
    can 'Give essay a letter grade (A,B,C,S,F)'
    give_grade(review: 'Review': str) -> 'Grade': str by llm();
}

with entry {
    # Example Essay
    example_essay = """
    The global power crisis is caused by high energy demand, old infrastructure, and reliance on fossil fuels.
    This crisis results in blackouts, higher costs for businesses, and problems for healthcare and education.
    To fix this, we need to use more renewable energy like solar and wind, update infrastructure, and use energy
    more efficiently. Better governance and regulations can help manage the crisis and attract investments for a
    stable energy future.
    """;

    # Convert essay into EssayObj
    essay = EssayObj(essay=example_essay);

    # Criteria for evaluation
    all_criterion = ["Clarity", "Coherency"];

    # Judgements dictionary to store evaluations
    judgements = {};

    # Evaluate the essay based on criteria
    for criterion in all_criterion {
        judgement = essay.essay_eval(criterion);
        judgements[criteria] = judgement;
    }

    # Generate a review based on judgements
    review = essay.generate_review(judgements);

    # Generate a grade based on the review
    grade = essay.give_grade(review);

    # Output
    print("Evaluator's Remarks: ", review);
    print("Grade: ", grade);
}
