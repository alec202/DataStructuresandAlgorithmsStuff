"""
Second solution, using merge sort idea to add
numbers in order ascending. Due this by using the bisect library.

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

from sortedcontainers import SortedList
from statistics import mean
class MKAverage:
    def __init__(self, m: int, k: int):
        self.stream = []
        self.m = m
        self.k = k
        self.sortedNums = SortedList()

    def addElement(self, newNum: int) -> None:
        # if len(self.stream) < (2 * self.k):
        #     self.stream.append(newNum)
        # insert the new number into self.stream in a way that maintains sorted order.
        self.stream.append(newNum)
        self.sortedNums.add(newNum)
        if len(self.sortedNums) > self.m:
            valToRemove = self.stream.pop(0)
            self.sortedNums.remove(valToRemove)



    def calculateMKAverage(self) -> int:
        # if self.stream is less than m return -1.
        if len(self.stream) < self.m:
            return -1
        # self.stream was bigger than m, so copy last m elements
        else:
            # self.sortedNums is already in sorted order
            numsForAvg = self.sortedNums[self.k:-self.k]
            return int(mean(numsForAvg))






# Your MKAverage object will be instantiated and called as such:
# obj = MKAverage(m, k)
# obj.addElement(num)
# param_2 = obj.calculateMKAverage()


obj = MKAverage(3, 1)
obj.addElement(3)  # current elements are [3]
obj.addElement(1)  # current elements are [3,1]
print(obj.calculateMKAverage())  # return -1, because m = 3 and only 2 elements exist.
obj.addElement(10)  # current elements are [3,1,10]
print(obj.calculateMKAverage())  # The last 3 elements are [3,1,10].
# After removing smallest and largest 1 element the container will be [3].
# The average of [3] equals 3/1 = 3, return 3
obj.addElement(5)  # current elements are [3,1,10,5]
obj.addElement(5)  # current elements are [3,1,10,5,5]
obj.addElement(5)  # current elements are [3,1,10,5,5,5]
print(obj.calculateMKAverage())  # The last 3 elements are [5,5,5].
# After removing smallest and largest 1 element the container will be [5].
# The average of [5] equals 5/1 = 5, return 5


