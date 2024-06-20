import lmql
import asyncio

@lmql.query
async def predict_new_map(previous_map: str, time_taken: int, hardness: int, win_death_ratio: float):
    '''
    lmql
    "Given the previous map:\n\n{previous_map}\n\nwith time taken: {time_taken} minutes, hardness level: {hardness}, and win/death ratio: {win_death_ratio}, predict a new map with similar structure and adjusted hardness. Return the map as a list of strings where each string represents a row."
    '''

async def main():
    previous_map = """
    ....B....
    ...E.E...
    ....B....
    ...P.....
    .........
    """
    time_taken = 10
    hardness = 20
    win_death_ratio = 5.0

    new_map = await predict_new_map(previous_map, time_taken, hardness, win_death_ratio)
    for row in new_map:
        print(row)

if __name__ == "__main__":
    asyncio.run(main())
