import:py from jaclang.core.llms, Anthropic;

glob llm = Anthropic(model_name="claude-3-sonnet-20240229", max_tokens=300);


glob evaluation_criteria = [
    'Thesis Statement - range of marks(0-10)', 
    'Clarity of Argument - range of marks(0-10)', 
    'Organization - range of marks(0-10)', 
    'Supporting Evidence - range of marks(0-10)', 
    'Analysis and Critical Thinking - range of marks(0-10)', 
    'Use of Language - range of marks(0-10)', 
    'Grammar and Mechanics - range of marks(0-10)', 
    'Originality and Creativity - range of marks(0-10)', 
    'Engagement of the Reader - range of marks(0-10)', 
    'Conclusion - range of marks(0-10)'];


glob grade_ranges = "A (if marks 100-75), B (if marks 74-65), C (if marks 64-55), S (if marks 54-35), F (if marks 34-0)";


# Methods defined for grading
can 'Evaluate the given essay based on the given criteria. Provide Detailed Evaluation.'
evaluate_essay(essay:'the essay provided by the user' :str, 
               evaluation_criteria:'Thease are the evaluation criterias.' :list) -> 'evaluation': str by llm();


can 'Based on the evaluation details, give a grade letter (A,B,C,S,F)'
grade_essay(evaluation:'Evaluation details of the essay' :str, 
               grading_range:'This is the grade should be given according to there marks' :str) -> 'grade': str by llm();


can 'Generate a small remark with important points.'
remark_essay(evaluation:'Evaluation details of the essay' :str, 
            grade:'This is the received grade' :str) -> 'remark': str by llm();




with entry {
    
    # Sample Essay
    essay = "Reading enriches our lives by exposing us to new ideas and perspectives. It improves our vocabulary, enhances communication skills, and boosts cognitive functions. By fostering empathy and expanding our knowledge, reading is a simple yet powerful tool for personal growth.";


    # Methods calling
    evaluation = evaluate_essay(essay, evaluation_criteria);
    grade = grade_essay(evaluation, grade_ranges);
    remark = remark_essay(evaluation, grade);

    print("Grade: ", grade);
    print("Remark: ", remark);
}