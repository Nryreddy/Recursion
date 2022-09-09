n = int(input('enter the value of n -'))
m=n
for i in range(m):
    print(f" "*(m)+f"{i}"*i)
    m=m-1

for i in range(n):
    print(f"{i}"*i)

for i in range(1,n):
    print(f" "*(n)+f"{i} "*i)
    n = n - 1