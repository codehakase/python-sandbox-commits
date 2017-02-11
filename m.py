### SOLUTION1( fibonacci(nth-term): Point 'n Kill') ###
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-2) + fibonacci(n-1)

n = input("Enter a number \n")
n = int(n); index = 1; c = 1
while c <= n :
    print(str(c) + "\n")
    index = index+1
    c = fibonacci(index)

### SOLUTION2(for speed : Kill 'n run') ###
def fibonacci(n):
    _n1 = 0; _n2 = 1; _n3 = 1
    while _n3 <= n :
        print(str(_n3) + "\n")
        _n3 = _n1 + _n2
        _n1 = _n2
        _n2 = _n3

n = input("Enter a number \n")
fibonacci(int(n))
