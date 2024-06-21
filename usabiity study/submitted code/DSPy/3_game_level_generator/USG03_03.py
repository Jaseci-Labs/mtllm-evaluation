# import dspy

# # Setup Ollama environment
# ollama_mistral = dspy.OllamaLocal(model='phi3:3.8b')
# dspy.settings.configure(lm=ollama_mistral)

# levelmap = [
#         'BBBBBBBBBBBBBBBBBBBB',
#         'B...E..............B',
#         'B.......B..........B',
#         'B....BBBB..........B',
#         'B..................B',
#         'B..................B',
#         'B.........P........B',
#         'B..................B',
#         'B.............E....B',
#         'B..................B',
#         'B..................B',
#         'B.........B........B',
#         'B.........B........B',
#         'B.........B........B',
#         'BBBBBBBBBBBBBBBBBBBB'
#     ];

# classify = dspy.Predict('levelmap -> harderlevelmap')
# classify(levelmap=levelmap).harderlevelmap
import dspy

# Setup Ollama environment
# ollama_mistral = dspy.OllamaLocal(model='phi3:3.8b')
# dspy.settings.configure(lm=ollama_mistral)

llm = dspy.OpenAI(model="gpt-4o")
dspy.settings.configure(lm=llm)


levelmap = [
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

# Convert levelmap list to a string
levelmap_str = "\n".join(levelmap)

classify = dspy.Predict("levelmap -> harderlevelmap")
result = classify(levelmap=levelmap_str)

# Convert the result to the desired format
result_map_str = (
    "["
    + ",\n".join(["'" + row + "'" for row in result.harderlevelmap.split("\n")])
    + "];"
)

# Display the result
print(result_map_str)
