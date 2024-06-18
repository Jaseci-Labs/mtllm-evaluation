glob llm = OpenAI();

walker essay_evaluator {
    has essay:str;

    can review_essay {
        report {remarks: llm.prompt("Generate a brief remark for the following essay: " + essay)};
        report {grade: llm.prompt("Grade the essay with A, B, C, S, or F: " + essay)};
    }
}

walker init {
    root spawn essay_evaluator := essay_evaluator {
        essay: "This is a sample essay to test the evaluation system."
    };
    take = essay_evaluator.review_essay;
    print(take)
}
