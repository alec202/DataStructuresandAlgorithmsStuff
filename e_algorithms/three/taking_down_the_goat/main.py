# Bring this sucka down
# the tubes are organized in a striaght line, not in a circle


tubes_data = input().strip().split()
num_tubes = int(tubes_data[0])
numBoomTubes = int(tubes_data[1])
# Now we got all the data about the tubes in the correct format we want

# Lets get the data on the tubes that will explode
boomTubesData = input().split()
boomTubesInts = [int(boomTubesData[i]) for i in range(0, len(boomTubesData))]
# now we got all the tubes that will explode as integers

# lets make the function that will solve this problem
def safest_distance(numTubes: int, numBadTubes: int, bombTubes: list[int]):
    # if every tube is going to blow up, then there's no safe route so just return 0. We know
    # if there's no safe route because numTubes will equal the number of bad tubes
    if numTubes == numBadTubes:
        return 0
    else:
        # there's at least 1 safe tube
        # sort the bombTubes
        bombTubes.sort()
        # we want to consider the scenario where the first or last tube is the best to take (if
        # they aren't a bomb as well:
        # Lets first consider if the first tube isn't a bomb, and may be the best tube to take
        if bombTubes[0] != 0:
            best_distance = bombTubes[0]
        else:
            # 0 tube is a bomb, we need to initialize best_distance for comparison if end tube
            # isn't a bomb, let's just initialize it with -10, since the best_distance has to be
            # greater than -10
            best_distance = -10
        # Lets look at if the last tube isn't a bomb and is the best to take
        last_tube = numTubes - 1
        if bombTubes[-1] != last_tube:
            distance = last_tube - bombTubes[-1]
            if distance > best_distance:
                best_distance = distance



        # below will find the best distance, assuming the best tube is between the bombs.
        # This doesn't find if one of the endpoints are the best tube (we already did this above)
        # let's utilize two pointers to determine the median distance between the 2 tubes
        # lets also update our best distance variable as we go as well.
        for i in range(1, len(bombTubes)):
            j = i - 1
            distFromBomb = bombTubes[i] - bombTubes[j]
            middle_of_bombs = distFromBomb // 2
            if middle_of_bombs > best_distance:
                best_distance = middle_of_bombs


        # Best distance has been found, lets return that
        return best_distance
# let's call the function we made to solve this problem
print(safest_distance(num_tubes, numBoomTubes, boomTubesInts))
"""
num_tubes = 20
bombTubes = 1, 6, 10, 11, 13
numBadTubes = 5
best_distance = 1
last_tube = 19
distance = 6        (because 19 - 13)
i = 
j = 

"""








