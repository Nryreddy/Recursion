def r_fact(n):  # recursion
    assert n>=0 and int(n)==n , 'enter only positive integer'
    if n in [0, 1]:
        return 1
    else:
        return n * r_fact(n - 1)


y = r_fact(5)
print(y)











def fac(n):        # iteration method
    m = 1
    for i in range(1, n + 1):
        m = m * i
    return m

k = fac(10)