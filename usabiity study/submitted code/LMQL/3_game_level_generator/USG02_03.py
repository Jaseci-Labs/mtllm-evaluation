import lmql


@lmql.query
def generate_harder_map(
    previous_map: str, time_taken: int, hardness_level: int, win_death_ratio: float
):
    '''lmql
    argmax
        harder_map = """
        Previous Level Map:
        {previous_map}
        Time Taken: {time_taken}
        Hardness Level: {hardness_level}
        Win/Death Ratio: {win_death_ratio}

        Generate a new level map with the same structure as the previous map, but harder:
        """
    clause
    '''
    pass


previous_map = """
P...B
..B..
...E.
E..B.
.B...
"""

time_taken = 120  # in seconds
hardness_level = 50  # on a scale of 1-100
win_death_ratio = 2.0  # wins per death

harder_map = generate_harder_map(
    previous_map, time_taken, hardness_level, win_death_ratio
)
print(harder_map)
