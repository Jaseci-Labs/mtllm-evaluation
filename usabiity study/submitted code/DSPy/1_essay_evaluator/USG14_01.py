import dspy

# from google.colab import userdata


class EssayEvaluation(dspy.Signature):
    """Evaluate a given essay according to the given criteria and give a grade and reasons to give that grade."""

    input_essay = dspy.InputField()
    main_criteria = dspy.InputField()
    evaluation_result = dspy.OutputField()


# OPENAI_API_KEY = userdata.get('OPENAI_API_KEY')

# turbo = dspy.OpenAI(model='gpt-3.5-turbo', max_tokens=1000, api_key=OPENAI_API_KEY)
# dspy.settings.configure(lm=turbo)

llm = dspy.OpenAI(model="gpt-4o")
dspy.settings.configure(lm=llm)

essay_evaluation_as_template = dspy.signatures.signature_to_template(EssayEvaluation)


class EssayEvaluator(dspy.Module):
    def __init__(self):
        super().__init__()
        self.prog = dspy.ChainOfThought(EssayEvaluation)

    def forward(self, input_essay, main_criteria):
        return self.prog(input_essay=input_essay, main_criteria=main_criteria)


evaluator = EssayEvaluator()

essay = input("Enter the essay to be evaluated: ")
criteria = input("Enter the main criteria for the evaluation: ")

result = evaluator.forward(input_essay=essay, main_criteria=criteria)
print(f"Grading for the essay: \n{result}")
