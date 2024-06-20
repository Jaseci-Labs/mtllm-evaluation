import:py from jaclang.core.llms, Ollama;

glob llm = Ollama(model_name = "llama2:latest");

obj Essay {
    has essay: 'Essay': str;

    can 'Evaluate the essay based on the given criteria. Provide evaluation of the essay'
    essay_judge(criteria: 'Criteria': str) -> 'Judgement': str by llm(incl_info=(self.essay));

    can 'Generate a summary'
    generate_summary(analysis: 'Analysis': dict) -> 'Summary': str by llm(incl_info=(self.essay));

    can 'Give essay a letter grade from only (A,B,C,D,S,F)'
    give_grade(summary: 'Summary': str) -> 'Grade': str by llm();
}

with entry{
    input_path = "/home/gayanukaa/llm-test/mtllm-test/essay/essay.txt";
    with open(input_path, 'r') as file {
        essay = file.read();
    }
    essay = Essay(essay);

    criterias = ["clarity", "coherency", "grammar"];
    analysis = {};
    for criteria in criterias {
        judgement = essay.essay_judge(criteria);
        analysis[criteria] = judgement;
    }
    summary = essay.generate_summary(analysis);
    grade = essay.give_grade(summary);
    output = summary + grade;
    output_path = "/home/gayanukaa/llm-test/mtllm-test/essay/evaluation.txt";
    with open(output_path, 'w') as file {
        file.write(output);
    }
}