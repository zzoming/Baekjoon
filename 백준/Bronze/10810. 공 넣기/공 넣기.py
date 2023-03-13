
N,M = map(int,input().split())
num = [0 for x in range(1,N+1)]
for i in range(M) :
    i,j,k = map(int,input().split())
    num[i-1:j] = [k]*(j-i+1)
print(*num)