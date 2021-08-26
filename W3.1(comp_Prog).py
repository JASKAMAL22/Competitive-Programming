def check(k):
    for n in k:
        c0=n.count('0')
        c1=n.count('1')
        if c1>c0:
            res.append(1)
        elif c1==c0:
            res.append(-1)
        else:
            res.append(0)

T=int(input())
j=0
res=[]
k=[]
while(j<T):
    S=input()
    j+=1
    S=list(S)
    l=len(S)
    c=S.count('1')
    p=0
    i=1
    while (i<l-1 or i==1) and p<c :
        if S[i]=='1' and S[i-1]=='0' :
            S[i-1]=2
            p+=1

        elif S[i]=='1' and S[i+1]=='0' :
            S[i+1]=2
            p+=1

        elif S[i]=='0' and S[i+1]=='1' :
            S[i]=2
            p+=1
        
        elif S[i]=='0' and S[i-1]=='1' :
            S[i]=2
            p+=1

        i+=1

    k.append(S)

check(k)
r=len(res)
for h in range(r):
    if h==r-1:
        print(res[h])
    else:
        print(res[h],end="\n")