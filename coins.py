COINS = [9, 6, 4, 1]

def memoize(func):
    func_val_cache = {}
    def wrapper(*args):
        key = args
        val = func_val_cache.get(key, None)
        if val:
            return val
        else:
            func_val_cache[key] = func(*args)
            return func_val_cache[key]
    return wrapper

@memoize
def make_change(amount):
    """This function returns the following 
        None if no change possible
        List of coin values (minimum possible to make the change) 
    """
    if amount < 0:
        return None
    elif amount == 0:
        return []

    #Now, we will select each coin from available types of coins
    #determine how many coins will be required for each of the coin value

    coin_sets = []
    for coin in COINS:
        remaining_amount = amount - coin
        if remaining_amount >= 0:
            #ignore this coin if remaining amount is negative
            curr_coin_set = [coin]
            #recursively make the change for remaining amount
            remaining_coins = make_change(remaining_amount)
            if remaining_coins is not None:
                curr_coin_set.extend(remaining_coins)
                coin_sets.append(curr_coin_set)

    #pick one set which is the minimum of all the combination
    if coin_sets:
        return min(coin_sets, key=lambda x: len(x))
    else:
        return []

if __name__ == '__main__':
    import sys
    if len(sys.argv) == 2:
        print make_change(int(sys.argv[1]))
    else:
        print "%s <amount to make change> e.g. python coins.py 35" % (sys.argv[0])
