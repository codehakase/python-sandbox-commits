# using memoization
fibonnaci_cache = {}
def fibonnaci2(n):
    # check if the value exist, then reuturns it
    if n in fibonnaci_cache:
        return fibonnaci_cache[n]
    # compute the nth term
    if n == 1:
        value = 1
    elif n == 2:
        value = 1
    elif n > 2:
        value = fibonnaci2(n-1) + fibonnaci2(n-2)
    # Cache the value and return it
    fibonnaci_cache[n] = value
    return value
