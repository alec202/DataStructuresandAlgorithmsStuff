"""
Original Unoptimized Solution

Solution Is TOO Slow For Leetcode to even grade.
Timed out on test case 13

You are given two integers, m and k, and a stream of integers. You are tasked to implement a data structure
that calculates the MKAverage for the stream.

The MKAverage can be calculated using these steps:

If the number of the elements in the stream is less than m you should consider the MKAverage to be -1.
Otherwise, copy the last m elements of the stream to a separate container.

Remove the smallest k elements and the largest k elements from the container.
Calculate the average value for the rest of the elements rounded down to the nearest integer.
Implement the MKAverage class:

MKAverage(int m, int k) Initializes the MKAverage object with an empty stream and the two integers m and k.
void addElement(int num) Inserts a new element num into the stream.
int calculateMKAverage() Calculates and returns the MKAverage for the current stream rounded down to the nearest integer.


"""
class MKAverage:

    def __init__(self, m: int, k: int):
        self.stream = []
        self.m = m
        self.k = k

    def addElement(self, num: int) -> None:
        self.stream.append(num)

    def calculateMKAverage(self) -> int:
        if len(self.stream) < self.m:
            return -1
        else:
            indexToSlice = len(self.stream) - self.m
            last_m_elements = self.stream[indexToSlice:]
            sortedNums = sorted(last_m_elements)
            upper_bound_k_elements = (len(sortedNums) - self.k)
            numsForAvg = sortedNums[self.k: upper_bound_k_elements]

            import statistics
            return int(statistics.mean(numsForAvg))

# Your MKAverage object will be instantiated and called as such:
# obj = MKAverage(m, k)
# obj.addElement(num)
# param_2 = obj.calculateMKAverage()


obj = MKAverage(3, 1)
obj.addElement(3)  # current elements are [3]
obj.addElement(1)  # current elements are [3,1]
print(obj.calculateMKAverage()) # return -1, because m = 3 and only 2 elements exist.
obj.addElement(10)  # current elements are [3,1,10]
print(obj.calculateMKAverage())  # The last 3 elements are [3,1,10].
# After removing smallest and largest 1 element the container will be [3].
# The average of [3] equals 3/1 = 3, return 3
obj.addElement(5)  # current elements are [3,1,10,5]
obj.addElement(5)  # current elements are [3,1,10,5,5]
obj.addElement(5)  # current elements are [3,1,10,5,5,5]
print(obj.calculateMKAverage() ) # The last 3 elements are [5,5,5].
# After removing smallest and largest 1 element the container will be [5].
# The average of [5] equals 5/1 = 5, return 5

