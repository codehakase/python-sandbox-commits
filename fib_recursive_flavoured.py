# fibonnaci function with better speed
# using recursion and memoization

# with ordinary recursion
def fibonnaci(n):
    if n ==1:
        return 1
    elif n ==2:
        return 1
    elif n > 2:
        return fibonnaci(n-1) + fibonnaci(n-2)

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



# Making adjustment to the previous fibonnaci() function by using LRUC (Least Recently Used Cache)
from functools import lru_cache
@Lru_cache(maxsize = 1000)
def fibonnaci3(n):
    if n ==1:
        return 1
    elif n ==2:
        return 1
    elif n > 2:
        return fibonnaci(n-1) + fibonnaci(n-2)

        for n in range(1, 1001):
            print(n, ":", fibonnaci3(n))
