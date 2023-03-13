num_list = []
for i in range(28) :
    num_list.append(int(input()))
num = []
for i in range(1,31) :
    if i not in num_list : 
        num.append(i)
print(min(num))
print(max(num))
        