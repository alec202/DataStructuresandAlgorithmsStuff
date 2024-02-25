import argparse

def exact_change_dp(x, coins):
    smallest_coin = min(coins)
    # If no coin is smaller than x, we can't make change for x.
    if x < smallest_coin:
        return None

    fewest_coins = [None for _ in range( x+1 )]
    fewest_coins[0] = 0 # Don't need any coins to make 0
    # Start with smallest coin value (all non-zero smaller values are impossible)
    for i in range(smallest_coin, len(fewest_coins)):
        # Can we use any of the coins to make the target?
        options = []
        for coin in coins:
            prev = i - coin # Best count without this coin
            count = fewest_coins[prev] if prev >= 0 else None
            if not count is None:
                options.append(count + 1)
        fewest_coins[i] = min(options) if len(options) > 0 else None

    return fewest_coins[i]

if __name__ == "__main__":
    # parser = argparse.ArgumentParser(description="Make change for target value using given coin values.")
    # parser.add_argument("--target", type=int, required=True, help="Target value to make change for")
    # parser.add_argument("--coins", type=int, required=True, nargs="+", help="Coin values to include")
    #
    # args = parser.parse_args()
    # target = args.target
    # coin_values = args.coins
    target = 30
    coin_values = [1, 5, 25]

    print(exact_change_dp(target, coin_values))
