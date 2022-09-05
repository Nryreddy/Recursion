def fibonacci(n):
    assert n>=0 and int(n) == n,'fibonacci number cannot be negative number or non-integer number'
    if n in [0,1]:
        return n
    else:
        return fibonacci(n-1)+fibonacci(n-2)

n= int(input('enter n - '))
print(f"the {n}th fibonacci number is "+str(fibonacci(n)))
for i in range(n+1):
    print(fibonacci(i))