import dspy
llm = dspy.OpenAI()
dspy.configure(lm=llm)
question = input()
answer = dspy.ChainOfThought('question -> answer')
response = answer(question=question)

print(response.answer)
