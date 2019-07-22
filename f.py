s1,2t=map(int,input().split())
for j in range(1,min(s1,2t)+1):
    if((s1%j==0) and (2t%j==0)):
        y=j
print(y)
