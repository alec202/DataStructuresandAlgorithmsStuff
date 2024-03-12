class Solution:

    output_arr = []

    def __init__(self):
        self.table = []

    def shorten(self, brick_lengths,i,old_index,length):
        if old_index >= length:
            return brick_lengths
        while old_index < length and brick_lengths[old_index] <= i:
            old_index += 1
        return brick_lengths[0:old_index]


    def dp (self, brick_lengths, length,brick_types):
        # table = [0 for _ in range(length+1)]
        self.table = [0] * (length+1)
        for i in brick_lengths:
            if i <= length:
                self.table[i] += 1

        lengthOflist = brick_types

        old_index = 0
        for i in range(brick_lengths[0],len(self.table)):
            sum = self.table[i]
            shorter_brick_lengths = self.shorten(brick_lengths,i,old_index,lengthOflist)
            old_index = len(shorter_brick_lengths)

            for x in shorter_brick_lengths:
                sum += self.table[i-x]
            self.table[i] = sum % 1000000009
        Solution.output_arr.append(f"{self.table[length] % 1000000009}")

if __name__ == "__main__":
    test_cases = int(input())

    for i in range(test_cases):
        test_case = input().split()

        brick_types = int(test_case[0])
        length = int(test_case[1])

        test_case2 = input().split()

        brick_lengths = [int(j) for j in test_case2]

        sol = Solution()
        sol.dp(brick_lengths,length,brick_types)

    print("\n".join(sol.output_arr))
