"""minimum and maximum are inclusive

Don't want to go 1 by 1 comparing each number since that is not fast enough.

In this challenge participants must think of a number with certain qualities and their opponents must guess what that number must be. This year the rules are:

All numbers must be a multiple of 12.
All numbers must be a perfect square.
All numbers must be within the boundaries (minimums and maximums) that are provided for the values.
So if the boundaries required that numbers be between 10 and 100, the number 36 would be allowed, but 49 would not (it is not a multiple of 12) nor would 60 (it is not a perfect square), or 144 (it is greater than the maximum).

Given the minimum value ( x ) and the maximum value ( y ) you must calculate how many of these values are divisible by 12 (d ), how many are perfect squares ( s ), and how many values have both qualities ( b ).

Write a program to perform these calculations.

Input Format

The first line contains T, the number of test cases to follow, each on a new line.

Each test contains two space-separated integers denoting the minimum ( x ) and the maximum ( y ) values allowed, inclusive.


With each test case on a new line, print out d, s, and b (where d is the number of values divisible by 12, s is the
number of perfect squares, and b is the number of values that meet both criteria

Sample Input:
2
6 12
25 37

Sample Output:
1 1 0
1 2 1
"""
import math

num_tests = int(input().strip())
# list comprehensions are faster than if we just did a traditional for loop to build a list (in general).
# now we've gathered all of the input.
tests = [input().split() for _ in range(num_tests)]
# with open("mernirvasNumberAnswer.txt", "r") as file:
#     line = file.readline()
# solve each test case
for test in tests:
    x = int(test[0])
    y = int(test[1])

    # # first figure out all numbers that are multiples of 12 between x and y.
    # div12 = [i for i in range(x, y+1) if (i % 12) == 0]
    # could figure out first number divided by 12 and last number divisible 12
    first_mult12 = math.ceil(x / 12)
    last_mult12 = math.floor(y / 12)
    num_div12 = (last_mult12 - first_mult12) + 1
    # another way we could do:
    # first_div12 = first_mult12 * 12
    # last_div12 = last_mult12 * 12
    # print(first_mult12, last_mult12)
    # print(first_div12, last_div12)
    # print(num_div12)

    # (2) figure out all numbers that are even squares
    first_square = math.ceil(math.sqrt(x))
    last_square = math.floor(math.sqrt(y))
    num_square = (last_square - first_square) + 1
    # (3) now we have to build a list of all of the numbers that have both properties.
    # Iterate over every square or iterate over the square
    # Iterating over the squares is faster than iteratin over the mults of 12.
    num_both = 0
    if num_square >= 1:
        # for i in range(first_mult12, last_mult12):
        #     if math.sqrt(i) %
        """This is O(N) time but it's still too slow. Is our solution supposed to be lg(n) or contsant
        somehow? Or how could I improve this solution?"""

        for i in range(first_square, last_square + 1):
            if i * i < (last_square + 1) ** 2:
                if i*i % 12 == 0:
                    num_both += 1
    your_output = " ".join([str(num_div12), str(num_square), str(num_both)])
    # print(f"\nx/lower bound = {x}, y/upper bound = {y}, and your_output = {your_output} while expected ans = {line}. type(your_output) = {type(your_output)} type(ans) = {type(line)}") if your_output != line else None
    print(your_output)



