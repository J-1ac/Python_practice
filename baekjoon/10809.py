s=str(input())
for i in range(97,123, 1):
    for j in range(len(s)):
        if chr(i) not in s:
            print("-1", end=" ")
            break
        if ord(s[j]) == i:
            print(j, end=" ")
            break