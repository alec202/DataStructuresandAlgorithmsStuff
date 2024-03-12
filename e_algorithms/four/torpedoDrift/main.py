# This solution was formed after watching this video: https://www.youtube.com/watch?v=dw2nMCxG0ik

def torpedoDrift(nums, target):
    cache = {0: 1}
    [cache.update({i: 0}) for i in range(1, target + 1)]
    # for i in range(1, target + 1):
    #     cache[i] = 0

    for i in range(1, target + 1):
        for num in nums:
            sub = i - num
            if sub >= 0:
                cache[i] += cache[sub]

    return cache[target]




if __name__ == "__main__":
    output_arr = []
    numTestCases = int(input())
    for i in range(0, numTestCases):
        numDifferentBricks, _, target = input().partition(" ")
        numDifferentBricks = int(numDifferentBricks)
        target = int(target)
        brickLengths = input().split()
        brickLengths = [int(brickLength) for brickLength in brickLengths]
        output_arr.append(f"{torpedoDrift(brickLengths, target) % 1000000009}")

    print("\n".join(output_arr))





