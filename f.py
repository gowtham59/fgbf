s1,t2=map(int,input().split())
for j in range(1,min(s1,t2)+1):
    if((s1%j==0) and (t2%j==0)):
        y=j
print(y)
