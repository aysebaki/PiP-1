def fib(n: int) -> int:
    if n == 0 or n ==1: return n
    elif n < 0: return -1

    fibo = [0,1]
    for ix in range (2, n+1):
        fibo.append(fibo[ix-1] + fibo[ix-2])
    return fibo[-1]

print(fib(0))
print(fib(1))
print(fib(2))
print(fib(3))
print(fib(7))
print(fib(-2))