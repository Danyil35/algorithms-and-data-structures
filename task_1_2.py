def fib_recursion(n):
    if n < 0:
        raise ValueError("The number must be greater than 0")
    if n in {0, 1}:
        return n
    else:
        return fib_recursion(n - 1) + fib_recursion(n - 2)



print(" ".join(map(str, [fib_recursion(i) for i in range(10)])))