N = int(input())
num = list(map(int,input().split()))
M = max(num)
num_list = []
for i in num :
    num_list.append((i/M)*100)
print(sum(num_list) / len(num_list))