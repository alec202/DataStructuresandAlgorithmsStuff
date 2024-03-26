"""In the Atlas Lift event, contestants must lift a giant stone replica of the Earth over their heads and hold it for
as long as possible. Every second the replica gets slightly heavier.

You are given the number of seconds each contestant can last. You must output the number of starting contestants,
and every time a contestant falls, the number of contestants that remain.

Suppose there are six contestants that are able to last the following number of seconds:

5 4 4 2 2 8

The first contests fall after two seconds and we are left with four others; the times remaining for those four are:

3 2 2 _ _ 6

The above step is repeated until no opponents are left
"""

def atlas_lift(contestants: int, secs: list[int]):
    print(contestants)
    dict_vals = {}
    # build our dictionary up with all 0s
    for i in range(1, 1_001):
        dict_vals[i] = 0
        # lets loop through the array, get the dictionary key the array element coresponds to and + 1
    for i in range(0, contestants):
        dict_vals[secs[i]] += 1
    # Now our dictionary is a key which is the number of seconds and the value is the number of contestants who can hold
    # the stone for that long

    # Loop through dictionary and if the value is greater than 0 we want to subtract the amount and print
    # out the number of contestants remaining
    for i in range(1, 1_001):
        if dict_vals[i] > 0:
            contestants -= dict_vals[i]
            # if number of contestants = 0, return out of loop
            if contestants == 0:
                return
            print(contestants)


if __name__ == "__main__":
    num_contestants = int(input("Number of contestants? "))
    seconds_per_contestant = input("seconds each contestant can last? ").split()
    # Is the data being passed to our function as a list of nums or list of strings?
    for i in range(0, len(seconds_per_contestant)):
        seconds_per_contestant[i] = int(seconds_per_contestant[i])
    atlas_lift(num_contestants, seconds_per_contestant)


