import sys
#입력할 숫자 개수 입력 
n = int(sys.stdin.readline())
array = [0] * 10001


for i in range(n) :
    #숫자 입력 
    data = int(sys.stdin.readline())
    array[data] += 1 

for i in range(10001) :
    if array[i] != 0 :
        for j in range(array[i]) :
            print(i)