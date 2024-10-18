import dspy

llm = dspy.OpenAI(model='gpt-4o', max_tokens=1000)

dspy.configure(lm=llm)

question = input()
answer = dspy.TypedChainOfThought('question:str -> answer:int', max_retries=1)
response = answer(question=question)

print(response.answer)