import lmql

llm = lmql.model('openai/gpt-3.5-turbo-instruct')

@lmql.query(model=llm)
def sentiment_analysis(criteria):
    '''lmql
    "Q: In English, what is the sentiment of the following analysis of the essay based on this criteria: ```{criteria}```?\\n"
    "A: Let's think step by step. The review expresses a [SENTIMENT] sentiment. Explanation: [ANALYSIS]" where (len(TOKENS(ANALYSIS)) < 100) and STOPS_AT(ANALYSIS, '\\n') \
        and (SENTIMENT in ["A","B","C","D","S","F"])
    '''

input_path = '/home/jay_desk/REPOs/mtllm-evaluation/usabiity study/submitted code/LMQL/1_essay_evaluator/essay.txt'
with open(input_path, 'r') as file:
    essay = file.read()

criterias = ['clarity', 'coherency', 'grammar']
analysis = {}

for criteria in criterias:
    judgement = sentiment_analysis(f"The essay's {criteria} is: {essay}").variables['SENTIMENT']
    analysis[criteria] = judgement

@lmql.query(model=llm)
def generate_summary(analysis):
    '''lmql
    "Q: In English, summarize into a paragraph the following analysis: ```{analysis}```?\\n"
    "A: The summary of the analysis is: [SUMMARY]" where (len(TOKENS(SUMMARY)) < 100) and STOPS_AT(SUMMARY, '\\n')
    '''
summary = generate_summary(str(analysis)).variables['SUMMARY']

@lmql.query(model=llm)
def give_grade(summary):
    '''lmql
    "Q: Based on the following summary, what grade would you give the essay? ```{summary}```?\\n"
    "A: The grade for the essay is: [GRADE]" where (GRADE in ['A', 'B', 'C', 'D', 'S', 'F']) and STOPS_AT(GRADE, '\\n')
    '''
grade = give_grade(summary).variables['GRADE']

output = summary + "\nGrade: " + grade

output_path = '/home/jay_desk/REPOs/mtllm-evaluation/usabiity study/submitted code/LMQL/1_essay_evaluator/evaluation.txt'
with open(output_path, 'w') as file:
    file.write(output)

print(output)
