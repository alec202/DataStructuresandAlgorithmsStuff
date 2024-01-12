"""
In Nortia Racing contestants ride in robotic chariots that have two buttons, each representing a distance that it
should move forward. When a race starts, contestants must quickly press a series of buttons to get as close to a target
 as possible, so they want to know their options ahead of time.

You are given the distance forward that each button will take the chariot (x and y) and the number of times buttons
must be pressed (n). You should come up with the set of all possible distances that a contestant can travel after
exactly n presses
"""

tracked = []

def nortiaRacing(dist1, dist2, num_pushes):
    nortiaRacingHelper(dist1, dist2, num_pushes, 0)
    return

def nortiaRacingHelper(dist1: int, dist2: int, num_pushes: int, total:int) -> str:
    if num_pushes == 0:
        if total not in tracked:
            tracked.append(total)
        return
    else:
        nortiaRacingHelper(dist1, dist2, num_pushes - 1, total + dist1)
        nortiaRacingHelper(dist1, dist2, num_pushes - 1, total + dist2)
        return

if __name__ == "__main__":
    num_cases = int(input()) # num times to test data
    output_arr = []
    for i in range(0, num_cases):
        entry_data = input().split()
        dist1 = int(entry_data[0]) # distance of first button
        dist2 = int(entry_data[1]) # distance of second button
        num_pushes = int(entry_data[2]) # number of pushes for this test case
        nortiaRacing(dist1, dist2, num_pushes)
        for num in sorted(tracked):
            output_arr.append(num)
        output_arr.append("\n")
        tracked = []

    for item in output_arr:
        print(item, end=" ") if item != "\n" else print()

