class LMQL:
    @staticmethod
    def query(query):
        # Placeholder for querying a language model
        return "Generated map based on LMQL query"


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

    # Construct query using input parameters
    query = f"Generate a harder map based on previous map: {previous_map}, time taken: {time_taken}, hardness level: {hardness_level}, win/death ratio: {win_death_ratio}"

    # Query LMQL to generate a new map
    new_map = LMQL.query(query)

    # Display the generated map
    print("Generated map:")
    print(new_map)
