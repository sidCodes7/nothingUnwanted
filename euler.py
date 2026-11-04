def euler(n):
    if n<=2 or n%2==0:
        return False
    else:
        x = pow(2, (n-1)//2, n)
        return x == 1 or x == n-1

n = (int)(input("n: "))

if euler(n)==True:
    print("Prolly prime")
else:
    print("Composite")

#can iterate a from 2 to n-2