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
    for i in range(1, max(secs) + 1):
        pr = False
        for inx in range(0, len(secs)):
            if isinstance(secs[inx], int) and secs[inx] < i:
                contestants -= 1
                secs[inx] = ""
                pr = True
        if pr:
            print(contestants)



if __name__ == "__main__":
    num_contestants = int(input("Number of contestants? "))
    seconds_per_contestant = input("seconds each contestant can last? ").split()
    # Is the data being passed to our function as a list of nums or list of strings?
    for i in range(0, len(seconds_per_contestant)):
        seconds_per_contestant[i] = int(seconds_per_contestant[i])
    atlas_lift(num_contestants, seconds_per_contestant)


