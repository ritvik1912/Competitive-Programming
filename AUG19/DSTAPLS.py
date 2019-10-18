for _ in range(int(input())):
    n,k = list(map(int,input().strip().split()))
    temp = n//k
    if temp%k==0:
        print("NO")
    else:
        print("YES")
