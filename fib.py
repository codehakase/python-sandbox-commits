# fibonnaci sequence using recursion, loop and generators

# using recursion

def fib(n):
    if n == 1 or n == 2:
        return 1
    return fib(n-1) + fib(n-2)


# Using loops
def fibL(n):
    a = 1
    b = 1
    for i in range(n-1):
        a, b = b, a + b
    return a # current fibonnaci num

# Using generators
def fibG():
    a,b = 1,1
    while True:
        yield a
        a,b = b, a + b

# the output (recursion)
# for i in range(1, 20):
#     print fib(i)

# Test using loops
for i in range(1, 10):
    print fibL(i)
# Test using generators
# n = 0
# for i in fibG():
#     if n >= 10:
#         break
#     print (i)
#     n += 1
