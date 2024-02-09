"""
PROBLEM DESCRIPTION:
Taking down the Goat
Agent Ω has found the Goat's underground base of operations, and he is now fleeing his underground mansion to the
 surface of Mars. Ω needs to catch him there.

There are N escape tubes to the surface, all in a line evenly-spaced 1 meter apart. The goat has rigged a subset of
those tubes to explode, so Agent Ω needs to avoid those tubes or any other tubes even near them, if possible.
Given a list of tubes set to explode, can you identify the distance of the tube furthest from the nearest explosion?

Input Format

The first line has two values: N (the number of tubes, labeled 0 through N-1) and
K (the number of tubes set to explode). The next K values indicate the tube numbers that will explode. For example,
if there are 100 tubes with tubes 10, 60, and 95 set to explode, then Agent Ω would take tube 35, which
would be 25 meters away from the nearest exploding tube.

Constraints

1 ≤ N ≤ 109
1 ≤ K ≤ 105
0 ≤ explosion positions < N
Output Format

Output a single number indicating the farthest Agent Ω can be to the nearest exploding tube.

Example 1
Sample Input
5 2
0 4

Sample Output
2

Explanation

Five tubes are available (0, 1, 2, 3, 4), with explosions at tubes 0 and 4.
If Agent Ω attempts to take tube 2, she will be two meters away from any explosion, which is the best possible.

Example 2
Sample Input
6 6
0 1 2 4 3 5

Sample Output
0

Example 3
Sample Input
20 5
13 1 11 10 6

Sample Output
6

Example 4
Sample Input
90 17
4 76 16 71 56 7 77 31 2 66 12 32 57 11 19 14 42

Sample Output
12
"""

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








