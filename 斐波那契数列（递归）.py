def fib(n) :
    if n == 0 :
        return 0
    if n == 1 :
        return 1
    b = fib(n-1) + fib(n-2)
    return b
for i in range (100) :
    print(i,fib(i))