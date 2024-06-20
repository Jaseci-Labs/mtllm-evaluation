class MTLLM:
    @staticmethod
    def multi_task_learning(time_taken, hardness_level, win_death_ratio):
        # Placeholder for multi-task learning using MTLLM
        return "Generated map based on multi-task learning"

# Get input map from the user
def get_input_map():
    print("Enter the previous map (each row separated by a newline):")
    previous_map = []
    for _ in range(6):  # Assuming the map size is fixed (adjust as needed)
        row = input().strip()
        previous_map.append(row)
    return previous_map

# Example usage
if __name__ == "__main__":
    # Manually get input map from the user
    previous_map = get_input_map()

    # Example inputs (dummy values)
    time_taken = 30  # Minutes
    hardness_level = 75  # Scale of 1-100
    win_death_ratio = 3.5  # Win/death ratio

    # Perform multi-task learning using MTLLM
    new_map = MTLLM.multi_task_learning(time_taken, hardness_level, win_death_ratio)

    # Display the generated map
    print("Generated map:")
    print(new_map)
