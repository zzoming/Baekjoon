a = input()
a = [x for x in a]
o = []
for i in range(97,123) :
    if chr(i) in a :
        o.append(a.index(chr(i)))
    else : 
        o.append(-1)    
print(*o)
        