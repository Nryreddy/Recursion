def deciToBin(n):

    if n>=1:
        deciToBin(n//2)
    print(n%2,end='')

def deciToBin1(n):

    if n==0:
        return 0
    return n%2 + 10 * deciToBin1(n//2)


print(deciToBin(10))

print(deciToBin1(10))



