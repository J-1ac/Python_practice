x,y=input().split()
revx,revy="",""
for c in x:
    revx=c+revx
for c in y:
    revy=c+revy
xy,revxy=str(int(revx)+int(revy)),""
for c in xy:
    revxy=c+revxy
print(int(revxy))