"""In the year 2086, the eccentric trillionaire Octavian Heximus founded the Martian Olympics. Below are a series of
events that he included. Your job is to write programs to help players strategize the best moves to make in the
different games.

In the betting game "Discordian Poker", the level of each player’s bet changes every round until one player wins.

If your current bet is odd, it goes down by $15, but the remaining amount must be doubled.
If your current bet is even, it goes down by $99, but the remaining amount must be tripled.
If your bet would pass $1,000,000, it loops back around (so a bet of $1,000,007 just becomes $7). Likewise, any bet that
goes below $0 ALSO loops around (so a bet of -$7 would become a bet of $999,993).
Given a starting bet ( S ) and a specified number of rounds played ( k ), determine what your final bet will be at the
 end of the game.

Input Format The first line is a number ( T ), indicating the number of test cases. The next T lines each have two
values, S and k, indicating the starting bet and the number of rounds the game goes, respectively.

"""
def discordian_poker(s: int, k: int, count: int) -> None:
    # k = 5
    # s = 999972
    # count = 2
    if count > k:
        return s
    else:
        # if current bet is odd
        if s % 2 == 1:
            s -= 15
            s *= 2
        # Current bet is even
        else:
            s -= 99
            s *= 3
        # A question to ask is if S can ever 2,000,000 and above?
        # Yes it can 999,998
        # check if bet is above allowed range and fix it if so
        while s > 1_000_000:
            s -= 1_000_000
        # check if bet is negative, and fix it if so.
        while s < 0:
            s += 1_000_000
        # Incremenet count by 1
        count += 1
        return discordian_poker(s, k, count)







if __name__ == "__main__":
    num_tests = int(input())

    for test_idx in range(num_tests):
        line = input().split()
        s = int(line[0]) # Starting bet
        k = int(line[1]) # Number of rounds
        print(discordian_poker(s, k, 1))