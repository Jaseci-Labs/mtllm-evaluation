import dspy

class HarderLevelMap(dspy.Signature):
    """Generate a harder level map based on previous level map, time taken, hardness level, and win/death ratio"""
    
    current_level = dspy.InputField()
    time_taken = dspy.InputField()
    hardness_level = dspy.InputField()
    win_death_ratio = dspy.InputField()
    new_level = dspy.OutputField()

class LevelHardness(dspy.Signature):
    """Determine the hardness of the level"""
    
    level_description = dspy.InputField()
    hardness = dspy.OutputField()

class LevelCompletionTime(dspy.Signature):
    """Estimate the time taken to complete the level"""
    
    level_description = dspy.InputField()
    time_estimate = dspy.OutputField()

# Configure the local model
ollama_model = dspy.OllamaLocal(model='phi3:3.8b')
dspy.settings.configure(lm=ollama_model)

llm = dspy.OpenAI(model="gpt-4o")
dspy.settings.configure(lm=llm)


# Initial level map
initial_level_map = [
    'BBBBBBBBBBBBBBBBBBBB',
    'B...E..............B',
    'B.......B..........B',
    'B....BBBB..........B',
    'B..................B',
    'B..................B',
    'B.........P........B',
    'B..................B',
    'B.............E....B',
    'B..................B',
    'B..................B',
    'B.........B........B',
    'B.........B........B',
    'B.........B........B',
    'BBBBBBBBBBBBBBBBBBBB'
]

# Dummy values for other parameters
time_taken = 10  # in minutes
hardness_level = 50  # scale of 1-100
win_death_ratio = 1.5  # example value

# Criteria for generating a harder level map
harder_level_criteria = "Generate a harder level map based on previous level map, time taken, hardness level, and win/death ratio. Start each string with B and end with B. Use only B,.,E,P characters. Output only the new level map"

# Functions for generating harder level, finding hardness, and estimating time
def generate_harder_level(current_level, time_taken, hardness_level, win_death_ratio):
    HarderLevelMap._doc_ = harder_level_criteria
    classifier = dspy.Predict(HarderLevelMap)
    result = classifier(
        current_level=current_level,
        time_taken=time_taken,
        hardness_level=hardness_level,
        win_death_ratio=win_death_ratio
    )
    return result.new_level

def find_hardness(level):
    hardness_criteria = "Determine the hardness of the level. B for obstacles, '.' for walkable areas, 'E' for enemy characters, 'P' for player character. Output a hardness level from 1-100."
    LevelHardness._doc_ = hardness_criteria
    classifier = dspy.Predict(LevelHardness)
    result = classifier(level_description=level)
    return result.hardness

def estimate_completion_time(level):
    time_criteria = "Estimate time taken in minutes to complete the level. B for obstacles, '.' for walkable areas, 'E' for enemy characters, 'P' for player character. Output only a number."
    LevelCompletionTime._doc_ = time_criteria
    classifier = dspy.Predict(LevelCompletionTime)
    result = classifier(level_description=level)
    return result.time_estimate

# Generate the next harder level, find its hardness, and estimate the time to complete
next_level_map = generate_harder_level(initial_level_map, time_taken, hardness_level, win_death_ratio)
hardness = find_hardness(next_level_map)
time_estimate = estimate_completion_time(next_level_map)

print("Next Level Map:", next_level_map)
print("Level Hardness:", hardness)
print("Estimated Time to Complete:", time_estimate)
