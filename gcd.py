def gcd(n,m):
    assert int(n) == n and int(m) == m, 'enter only positive integer for exponent'
    if n<0:
        n=-1*n
    if m < 0:
        m = -1 * m
    if m==0:
        return n
    else:
        return int(gcd(m,n % m))


print(gcd(75,100))