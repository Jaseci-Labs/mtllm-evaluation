tasks = ["Read a new book",
"Go hiking with friends",
"Complete the marketing report",
"Prepare for the presentation",
"Cook dinner for my family"]

import dspy

class Order(dspy.Signature):
    """test """
    
    sentence = dspy.InputField()
    grade = dspy.OutputField()

class TimeTaken(dspy.Signature):
    """test """
    sentence = dspy.InputField()
    grade = dspy.OutputField()

ollama_mistral = dspy.OllamaLocal(model='phi3:3.8b')
llm = dspy.OpenAI(model="gpt-4o")
dspy.settings.configure(lm=llm)


cri1 = "Categorize these into a number between 1-10 based on general public. 10 means least priority and 1 means high priority.No reasons"
cri2 = "estimate time in minutes taken to complete this task in general. output only a integer number with no reasons"
def performTask(criteria, para, time ):
    Order.__doc__ = criteria
    classify = dspy.Predict(Order)
    x=classify(sentence=para)
    lines = x.grade.split('\n')
    for line in lines:
        if line.startswith('Grade:'):
            return int(line.split(': ')[1])

def timeTask(criteria1, para):
    TimeTaken.__doc__ = criteria1
    classify = dspy.Predict(TimeTaken)
    x1=classify(sentence=para)
    return x1.grade


results = []
for num in range(len(tasks)):
    temp = []
    
    z = timeTask(cri2, tasks[num])
    y = performTask(cri1, tasks[num],z)
    temp.append(tasks[num])
    temp.append(y)
    temp.append(z)
    print(temp)
    results.append(temp)

