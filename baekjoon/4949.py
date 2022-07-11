while True:
    checkstr=input()
    if checkstr ==".":
        break
    stack=[]
    isbalance=True
    for i in range(len(checkstr)):
        if checkstr[i]=="(":
            stack.append(0)
        elif checkstr[i]=="[":
            stack.append(1)
        elif checkstr[i]==")":
            if len(stack)==0:
                isbalance=False
                break
            else:
                if stack.pop()!=0:
                    isbalance=False
                    break   
                else:
                    continue
        elif checkstr[i]=="]":
            if len(stack)==0:
                isbalance=False
                break
            else:
                if stack.pop()!=1:
                    isbalance=False
                    break   
                else:
                    continue
    if len(stack)!=0 or isbalance==False:
        print("no")
    else:
        print("yes")