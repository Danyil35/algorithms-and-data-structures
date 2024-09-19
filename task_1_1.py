def fib_cycle(n):
    if n <= 0:
        raise ValueError("The number must be greater than 0")
    
    for i in range(n):
        if i == 0:
            a = 0
        elif i == 1:
            b = 1
        else:
            a, b = b, a + b

        print(a if i == 0 else b, end="\t")
    
    print("\n")


fib_cycle(100)