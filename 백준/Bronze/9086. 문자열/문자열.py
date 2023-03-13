num = int(input())
a = [input() for x in range(num)]
for x in a :
    print(x[0],x[-1],sep ='')