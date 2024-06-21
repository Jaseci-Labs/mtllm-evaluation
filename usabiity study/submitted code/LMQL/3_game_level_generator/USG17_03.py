import lmql


@lmql.query
def new_map(old_map, points):
    """lmql
    "create a new list using the list given and make add more E letters in the middle of B letters if points are higher less E letters if points are lower, B - Block or Obstacles, Enemies and the Player cannot pass through, . - Walkable are for all characters, E - Enemy Character, P - Player Character" where STOPS_AT(NEWMAP,"\n")

    # return just the ANSWER to the caller
    return NEWMAP
    """


oldMap = input("Enter your map : ")
points = input("Enter the points : ")

print(new_map(oldMap, points))
print(new_map(oldMap, points))
