def power_of_num(n,p):
    assert p >= 0 and int(p) == p, 'enter only positive integer for exponent'
    if p==0:
        return 1
    elif p==1:
        return n
    else:
        return n * power_of_num(n,p-1)


print(power_of_num(-3,3))