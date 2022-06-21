n = int(input())
words=[]
for i in range(n):
    words.append(input())
sets = set(words)
newwords = list(sets)
newwords.sort(key= lambda x:(len(x), x))
for i in range(len(newwords)):
    print(newwords[i])