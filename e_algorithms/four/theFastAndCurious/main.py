#

# def fastAndCusrios(numNums: int, listOfNums: list[int]):
#     j = 0
#     jSum, iSum = 0, 0
#     for i in range(1, numNums, 2):
#         iSum += listOfNums[i]
#         jSum += listOfNums[j]
#         jSum += 2
#     if iSum > jSum:
#         return iSum
#     else:
#         return jSum

def fastAndCurious(n: int, nums: list[int]):
    if n == 1:
        return nums[0]
    else:
        choices = [nums[0], nums[1]]
        for i in range(2, n):
            take = choices[0] + nums[i]
            if take >= choices[1]:
                val = take
            else:
                val = choices[1]
            choices[0] = choices[1]
            choices[1] = val

        if choices[0] > choices[1]:
            return choices[0]
        else:
            return choices[1]








if __name__ == "__main__":
    n = int(input())
    listNums = input().split()
    listNums = [int(listNums[i]) for i in range(0, len(listNums))]
    print(fastAndCurious(n, listNums))

