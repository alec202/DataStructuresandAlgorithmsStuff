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



if __name__ == "__main__":
    # First get the number of job requests the agent will receive
    num_job_requests = int(input())

