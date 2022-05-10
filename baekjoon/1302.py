from collections import Counter

def bestseller(books):
    count = Counter(books)
    i=0
    max_count = count.most_common(1)[0][1]
    max = count.most_common(1)[0][0]
    maxlist=[]
    maxlist.append(max)
    for i in range(1, len(count.most_common(len(books)))):
        if count.most_common(len(books))[i][1] == max_count:
            maxlist.append(count.most_common(len(books))[i][0])
    maxlist.sort()
    print(maxlist[0])

N = int(input())
book_list =[]

for _ in range(N):
    book_list.append(input())

bestseller(book_list)