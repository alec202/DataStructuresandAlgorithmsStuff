"""
In Nortia Racing contestants ride in robotic chariots that have two buttons, each representing a distance that it
should move forward. When a race starts, contestants must quickly press a series of buttons to get as close to a target
 as possible, so they want to know their options ahead of time.

You are given the distance forward that each button will take the chariot (x and y) and the number of times buttons
must be pressed (n). You should come up with the set of all possible distances that a contestant can travel after
exactly n presses
"""


def nortiaRacing(dist1: int, dist2: int, num_pushes: int) -> str:
    dists = []
    for i in range(0, num_pushes + 1):
        dis = (dist1 * i) + (dist2 * (num_pushes - i))
        dists.append(dis) if dis not in dists else None
    dists = sorted(dists)
    for ind in range(len(dists)):
        dists[ind] = str(dists[ind])
    return dists





if __name__ == "__main__":
    num_cases = int(input()) # num times to test data
    output_arr = []
    for i in range(0, num_cases):
        entry_data = input().split()
        dist1 = int(entry_data[0]) # distance of first button
        dist2 = int(entry_data[1]) # distance of second button
        num_pushes = int(entry_data[2]) # number of pushes for this test case
        sorted_tracked = nortiaRacing(dist1, dist2, num_pushes)
        output_arr.append(sorted_tracked)
        tracked = []

    for arr in output_arr:
        print(" ".join(arr))
