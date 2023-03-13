N = int(input())
word = []
for i in range(N) :
    word.append(input())

word_list = list(set(word))
word_list.sort()
word_list.sort(key = lambda x : len(x))

for w in word_list :
    print(w)