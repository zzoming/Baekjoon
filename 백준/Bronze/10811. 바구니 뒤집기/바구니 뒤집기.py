N ,M = map(int,input().split())
num = [x for x in range(1,N+1)]

for n in range(M) :
    i,j = map(int,input().split())
    num[i-1:j] = num[i-1:j][::-1]

print(*num)