def deciToBin1(n):
    assert int(n) == n,'the parameter must be an integer only'
    if n==0:
        return 0
    return n%2 + 10 * deciToBin1(int(n//2))

#def deciToBin(n):
#
#     if n>=1:
#         deciToBin(n//2)
#     print(n%2,end='')
# print(deciToBin(10))

print(deciToBin1(100))



