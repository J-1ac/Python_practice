n=int(input())
for _ in range(n):
    text=input()
    isvpn=[]
    result=True
    for i in range(len(text)):
        if text[i]=="(":
            isvpn.append("1")
        elif text[i]==")":
            if len(isvpn)==0:
                result=False
            else:
                isvpn.pop()
    if len(isvpn)!=0:
        result=False

    if result:
        print("YES")
    else:
        print("NO")