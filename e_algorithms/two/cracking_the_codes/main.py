'''
Description
Once Agent Ω was able to access all of The Goat’s communications, she needed to setup a program to crack his encoded
 messages as quickly as possible. Given a list of when each message first arrives and how long it will take to crack,
 Ω will always start on the quickest message that she currently knows about. You must determine the average time
 between message arrival and when the message is actually cracked. The challenge is that only one message can be
 processed at a time, so others will often have to wait in the queue.

Note: Some input files are NOT sorted.

Input Format

The first line provides the value N, the total number of job request coming in. The next N lines each have
two values: the time the job arrives (Ti) and how long the job will take (Li) Note that the job list may be unsorted.

Constraints:
1 ≤ N ≤ 10^5
0 ≤ Ti ≤ 10^9
1 ≤ Li ≤ 10^9

Output Format:
Display the integer part of the minimum average time that the job took. Do not include any decimal places.

Example 0:
3
0 3
1 9
2 6

Output 0:
9

Explanation 0:
Three encrypted messages come in at time 0, time 1, and time 2, and they will take 3, 9, and 6 seconds to decrypt
respectively. Agent Ω will start on the first message at time zero (it's the only one she knows about) and will take
3 seconds to finish it. At time 3 she'll start on the third message (since it's the shortest one) and finish it at
 time 9 (3+6). Since this message came in at time 2, she would have taken 7 seconds to complete it (9-2). Finally,
 at time 9 she will start decrypting the second message, finishing it at time 18, for a total of 17 seconds spent
 on it since it first arrived (18-1).

Given that the completion times for the three decryptions were 3 seconds, 7 seconds, and 17 seconds, Ω would have
spent an average of (3+7+17)/3 = 9 seconds per job, which is what you would output.

'''

import heapq as hq

def crack_code_avg(all_reqs: list[tuple, tuple], n: int) -> int:
    # sort requests based on order received
    all_reqs.sort()
    curr_time, avg_sum, num_cracks, i = 0, 0, 0, 0
    order_in_crack_length = []
    while num_cracks != n and i < len(all_reqs):
        if all_reqs[i][0] > curr_time:
            curr_time = all_reqs[i][0]
        while i < len(all_reqs) and all_reqs[i][0] <= curr_time :
            # We will use below to make the heap that will be based on how fast it is to crack the message.
            # heapq builds a min heap though, we want the fastest times, so in reality we want a max heap. We can
            # Still use heapq to make a max heap if we multiple the time_to_crack value (index 0) by negative 1
            order_in_crack_length.append((-all_reqs[i][1], all_reqs[i][0]))
            i += 1
        hq.heapify(order_in_crack_length)
        cracked = hq.heappop(order_in_crack_length)
        curr_time += cracked[0] * -1
        avg_sum += (curr_time - cracked[1])
        num_cracks += 1

    return avg_sum // n





if __name__ == "__main__":
    # First get the number of job requests the agent will receive
    num_job_requests = int(input())
    # Could use heap to get the next message we should solve.
    # Overall Algorithm would become nlg(n) if we pop off elements from the heap as we use them.
    # Max time is 10^9. Could we just replace that value with 10^10? Or are we required to
    # do popping off the heap?
    # we're going to use a heap so we will need a list.
    all_reqs = []
    # Get all of the inputs

    for i in range(0, num_job_requests):
        # convert input to tuple
        req = input().strip().partition(" ")
        all_reqs.append((int(req[0]), int(req[2])))
    # list of tuples storing all the requests successfully created.
    print(crack_code_avg(all_reqs, num_job_requests))




