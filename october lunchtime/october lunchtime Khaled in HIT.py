t=int(input())
while(t):
    x=int(input())
    l=list(map(int,input().split()))
    n=x//4
    l.sort()
    k=0
    key=0
    h=0
    while(k<n):
        h+=1
        k+=1
    if(l[h]!=l[h-1]):    
        x1=l[h]
    else:
        key=1
    k=0
    while(k<n):
        h+=1
        k+=1
    if(l[h]!=l[h-1]):
        y1=l[h]
    else:
        key=1
    k=0
    while(k<n):
        h+=1
        k+=1
    if(l[h]!=l[h-1]):
        z1=l[h]
    else:
        key=1
    if(x1!=y1 and y1!=z1 and key==0):
        print(str(x1)+" "+str(y1)+" "+str(z1))
    else:
        print("-1")
    t-=1
