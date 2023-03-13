num_list = []
for i in range(10) :
    num_list.append(int(input()))
#나머지 리스트 
num = []
for i in num_list :
    num.append(i % 42) 
# 서로 다른 나머지 개수 출력 
print(len(set(num)))