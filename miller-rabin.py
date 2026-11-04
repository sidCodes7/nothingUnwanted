def mr(n,k):
    if n<=1:
        return False
    if n==2:
        return True
    if n%2==0:
        return False

    d = n-1
    s = 0

    while d%2==0:
        d//=2
        s+=1

    for a in range(2, k+2):
        x = pow(a,d,n)

        if x==1 or x==n-1:
            continue

        for i in range(s-1):
            x = (x*x)%n

            if x==n-1:
                break
        else:
            return False

    return True

n = int(input("n: "))
k = int(input("k: "))

if mr(n, k):
    print("Prolly prime")
else:
    print("Composite")