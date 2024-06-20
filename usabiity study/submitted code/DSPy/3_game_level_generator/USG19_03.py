import dspy
from dspy.datasets import CustomDataset

# Configuring the language model
# turbo = dspy.OpenAI(model='gpt-3.5-turbo')

# For this task, we do not necessarily need a retrieval model, so we can skip configuring RM.


turbo = dspy.OpenAI(model="gpt-4o")
dspy.settings.configure(lm=turbo)

class MapDataset(CustomDataset):
    def load_data(self):
        # Dummy data for illustration purposes
        self.data = [
            {
                'previous_map': [
                    "BBBBBBBBBBBBBBBB",
                    "B...E............B",
                    "B........B........B",
                    "B....BBBB........B",
                    "B................B",
                    "B...............B",
                    "B................B",
                    "B.............P..B",
                    "B................B",
                    "B..............E..B",
                    "B................B",
                    "B...............B",
                    "B........B........B",
                    "B.........B.......B",
                    "B.........B......B",
                    "BBBBBBBBBBBBBBBBBB"
                ],
                'time_taken': 300,
                'hardness_level': 50,
                'win_death_ratio': 1.5,
                'new_map': None  # This will be the output we need to generate
            }
        ]

dataset = MapDataset()
class GenerateHarderMap(dspy.Signature):
    previous_map = dspy.InputField()
    time_taken = dspy.InputField()
    hardness_level = dspy.InputField()
    win_death_ratio = dspy.InputField()
    new_map = dspy.OutputField()

class GenerateMapPipeline(dspy.Module):
    def __init__(self):
        super().__init__()
        self.generate_map = dspy.ChainOfThought(GenerateHarderMap)

    def forward(self, previous_map, time_taken, hardness_level, win_death_ratio):
        prediction = self.generate_map(
            previous_map=previous_map,
            time_taken=time_taken,
            hardness_level=hardness_level,
            win_death_ratio=win_death_ratio
        )
        return dspy.Prediction(new_map=prediction.new_map)

# Example map details for prediction
map_details = {
    'previous_map': [
        "BBBBBBBBBBBBBBBB",
        "B...E............B",
        "B........B........B",
        "B....BBBB........B",
        "B................B",
        "B...............B",
        "B................B",
        "B.............P..B",
        "B................B",
        "B..............E..B",
        "B................B",
        "B...............B",
        "B........B........B",
        "B.........B.......B",
        "B.........B......B",
        "BBBBBBBBBBBBBBBBBB"
    ],
    'time_taken': 300,
    'hardness_level': 50,
    'win_death_ratio': 1.5
}

# Generate the harder map
pred = compiled_pipeline(
    previous_map=map_details['previous_map'],
    time_taken=map_details['time_taken'],
    hardness_level=map_details['hardness_level'],
    win_death_ratio=map_details['win_death_ratio']
)

# Print the new harder map
print("New Harder Map:")
for line in pred.new_map:
    print(line)
