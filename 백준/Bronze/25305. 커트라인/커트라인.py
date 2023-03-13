n,k = map(int,input().split())
x = list(map(int,input().split()))
# 점수 정렬
x.sort(reverse = True)
#커트라인
print(x[k-1])