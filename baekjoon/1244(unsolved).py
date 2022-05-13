def changeswitch(student, switch):
    sex = student[0]
    number = student[1]
    if sex == 1:
        for i in range(1,len(switch)+1):
            if i >= number and i%number==0:
                if switch[i-1]==0:
                    switch[i-1]==1
                else:
                    switch[i-1]==0
    else:
        j=0
        while number+j<len(switch) and number-j>0:
            if switch[number-j-1] == switch[number+j-1]:
                #print(switch[number-j-1],switch[number+j-1])
                j+=1
            else:
                break
        a=number-j
        b=number+j
        for a in range(b):
            if switch[a-1]==0:
                switch[a-1]==1
            else:
                switch[a-1]==0
    return switch


switchnumber = int(input())
switch=[0]*switchnumber
switch.append(map(int,input().split()))
studentnumber = int(input())
student=[0]*studentnumber
for i in range(studentnumber):
    student[0], student[1] = map(int,input().split())
    switch = changeswitch(student, switch)
print(switch)