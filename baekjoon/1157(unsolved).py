def mostcount(s):
    max=0
    max_count=0
    alreadys=[]
    for i in range(len(s)):
        if s[i] in alreadys:
            continue
        count = s.count(s[i])
        alreadys.append(s[i])
        if max<count:
            max=count
            max_count = i
        elif max==count:
            return("?")
    return(s[max_count])
    
s1 = input()
s2 = s1.lower()
print(mostcount(s2).upper())