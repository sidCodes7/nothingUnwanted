def fermat(n):
    if n<=1:
        return False
    else:
        return pow(2, n-1,n) == 1

n = (int)(input("n: "))

if fermat(n)==True:
    print("Prolly prime")
else:
    print("Composite")

#can iterate a from 2 to n-2