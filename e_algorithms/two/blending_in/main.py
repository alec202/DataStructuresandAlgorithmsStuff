"""As Agent Ω starts hacking into more C.H.I.M.E.R.A. files, she needs to make sure that her online activity doesn’t
look suspicious. She decides to limit herself to always have her activity level be the same as the median users.
To do so, she monitors all other users as they join and leave the system and updates the median level of activity
as she goes. Warning: You might be working with a LOT of data!

The median of M numbers is defined as the middle number after sorting them in order if M is odd. Or it is the
average of the middle two numbers if M is even. You start with an empty number list. Then, you can add numbers to
the list, or remove existing numbers from it. After each add or remove operation, output the median.

Input Format

The first line is an integer, N, that indicates the number of operations. Each of the next N lines is
either a x or r x, with x being an integer. An a x indicates that the value x is inserted (added) into the set,
and r x indicates that the value x is removed from the set.

Constraints:
1 ≤ N ≤ 106
-2,147,483,649 ≤ x ≤ 2,147,483,648

Output Format:
For each operation:
If the operation is remove and the number x is not in the list, output "Wrong!" in a single line,
but make no other modifications to the set of numbers
If the operation is remove and the number x is in the list, output the median after deleting x in
a single line.

NOTE: If your median is 3.0, print only 3. And if your median is 3.50, print only 3.5.
Whenever you need to print the median and the list is empty, print "Wrong!".

Example 0
Sample Input:
7
r 1
a 1
a 2
a 1
r 1
r 2
r 1

Sample Output:
Wrong!
1
1.5
1
1.5
1
Wrong!

Explanation:
The list starts out empty, so the first input fails to remove anything and "Wrong!" is output.

The value 1 is then added, so the median is 1, which is printed.

The value 2 is then added, making the set [1, 2], and the median is 1.5.

Another 1 is added, making the set [1, 1, 2]. The median is now 1.

One of the 1's is removed, bringing the set back to [1, 2].

The 2 is removed, leaving only a single 1.

The final 1 is removed, meaning that there are no values left, resulting in a "Wrong!"


Example 1
50
a -2147483648
a -2147483648
a -2147483647
r -2147483648
a 2147483647
r -2147483648
a 10
a 10
a 10
r 10
r 10
r 10
r 100
r 100
r 100
r -2147483648
r 2147483647
r 10
a 1
a -1
a 1
a -1
r 1
r -1
r -1
r -1
r -1
r 1
r 1
r 0
a 0
a 1
a 2147483647
a 2
r 1
a 2147483646
r 2
a 2147483640
a 10
r 2
r 2
r 2
r 1
r 1
r 1
a 2147483640
a 2147483640
a -2147483648
a -2147483640
r 2147483640

Sample Output

-2147483648
-2147483648
-2147483648
-2147483647.5
-2147483647
0
10
10
10
10
10
0
Wrong!
Wrong!
Wrong!
Wrong!
-2147483647
Wrong!
-1073741823
-1
0
-1
-1
-1
-1073741823
Wrong!
Wrong!
-2147483647
Wrong!
Wrong!
-1073741823.5
0
0.5
1
1
2
1073741823
2147483640
1073741825
Wrong!
Wrong!
Wrong!
Wrong!
Wrong!
Wrong!
2147483640
2147483640
2147483640
1073741825
10

"""

from statistics import median
def blending_in():
    n = int(input())
    func = {"a": add_num, 'r': rem_num}
    traffic_dict = {}
    traff_list = []
    for i in range(n):
        command = input().partition(" ")
        action, num = (command[0], int(command[2]))
        print(func[action](num, traffic_dict, traff_list))

def add_num(num, traffict_dict, traff_list):
    if num in traffict_dict:
        traffict_dict[num] += 1
    else:
        traffict_dict[num] = 1
    traff_list.append(num)
    return median(traff_list)

def rem_num(num, traffic_dict, traff_list):
    r = traffic_dict.get(num, 'f')
    if r == 'f':
        return 'Wrong!'
    else:
        traffic_dict[num] -= 1
        if traffic_dict[num] <= 0:
            del traffic_dict[num]
        # make remove o(1) since this is an unsorted array
        ind = traff_list.index(num)
        traff_list.pop(ind)
        if len(traff_list) == 0:
            return 'Wrong!'
        else:
            return median(traff_list)




if __name__ == "__main__":
    blending_in()

