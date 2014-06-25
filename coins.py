from collections import namedtuple

Coins = namedtuple('Coins', ['quarters', 'nickels', 'dimes', 'pennies'])

def memoize(fn):
    results = {}
    def execute(*args, **kwargs):
        key = str(args) + str(kwargs)
        if key not in results:
            results[key] = fn(*args, **kwargs)
            return results[key]
        #return results[key]
        print "Ignoring: ", key
        return []
    return execute


@memoize
def coins_better(cents, quarters=None, dimes=None, nickels=None, pennies=None):
    if cents <= 0:
        return

    results = []

    cents_new = cents

    if quarters is None:
        quarters = cents_new / 25
    if quarters > 0:
        #print "Quarters: ", quarters
        results.extend(coins_better(cents, quarters=quarters-1, dimes=dimes, nickels=nickels,
                pennies=pennies))
        cents_new = cents_new - (quarters * 25)

    if dimes is None:
        dimes = cents_new / 10
    if dimes > 0:
        #print "Dimes: ", dimes
        results.extend(coins_better(cents, quarters=quarters, dimes=dimes-1, nickels=nickels,
                pennies=pennies))
        cents_new = cents_new - (dimes * 10)

    if nickels is None:
        nickels = cents_new / 5
    if nickels > 0:
        #print "Nickels: ", nickels
        results.extend(coins_better(cents, quarters=quarters, dimes=dimes, nickels=nickels-1,
                pennies=pennies))
        cents_new = cents_new - (nickels * 5)

    #if pennies is None:
    pennies = cents_new
    #if pennies > 0:
    #print "Pennies: ", pennies
        #coins_better(cents, quarters=quarters, dimes=dimes, nickels=nickels, pennies=pennies - 1)

    #print "Quarters: %s, Dimes: %s, Nickels: %s, Pennies: %s" % (quarters,
    #        dimes, nickels, pennies)
    results.extend([Coins(quarters, nickels, dimes, pennies)])
    return results

