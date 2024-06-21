import dspy

initialMap = [
    "BBBBBBBBBBBBBBBBBBBB",
    "B...E..............B",
    "B.......B..........B",
    "B....BBBB..........B",
    "B..................B",
    "B..................B",
    "B.........P........B",
    "B..................B",
    "B.............E....B",
    "B..................B",
    "B..................B",
    "B.........B........B",
    "B.........B........B",
    "B.........B........B",
    "BBBBBBBBBBBBBBBBBBBB",
]

ollama_mistral = dspy.OllamaLocal(model="phi3:3.8b")
dspy.settings.configure(lm=ollama_mistral)

llm = dspy.OpenAI(model="gpt-4o")
dspy.settings.configure(lm=llm)


values = "for the values use 'B' for obstacles,'.' for Walkable for all characters,'E' for Enemy characters,'P' for Player character"

# cri1 = "look at the input sentence and create a same sentence with the length of 20. Use 'B' for start and end of the string. The characters that can be used are "
cri1 = "look at the input string and change its characters to in a random manner'E' and 'B' and'.' . Don't change the original length of the string."


class Re(dspy.Signature):
    """test"""

    string = dspy.InputField()
    outputSentence = dspy.OutputField()


def reCreate(criteria1, para, values):
    Re.__doc__ = criteria1  # + values + "if 'P' is not in the given sentence don't use it.Use only one 'P' in a sentence. Don't give reasons"
    classify = dspy.Predict(Re)
    x1 = classify(string=para)
    lines = x1.outputSentence.split("\n")
    for line in lines:
        if line.startswith("Output Sentence:"):
            return line.split(": ")[1]


results = []
for num in range(len(initialMap)):
    temp = []

    y = reCreate(cri1, initialMap[num], values)
    m = list(y)
    while True:
        if len(m) < 20:
            m.append(".")
        else:
            break

    m[0] = "B"
    x = m[0:18]
    x.append("B")
    r = "".join(x)
    temp.append(r)
    results.append(temp)

results[0] = ["BBBBBBBBBBBBBBBBBBBB"]
results[-1] = ["BBBBBBBBBBBBBBBBBBBB"]
for item in results:
    print(item)
