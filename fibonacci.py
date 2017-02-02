def fibonacci(n):
    a = b = 1
    for i in range(1, n+1):
        c = a + b
        print b
        a = b
        b = c

print (fibonacci(10))
