import math
t=int(input())
while(t):
    x=int(input())
    l=list(map(int,input().split()))
    l1=[0]*100
    lf=[0]*100
    z=0
    while(z<x):
        k=1
        lf[z]=l1[l[z]]
        while(k<math.sqrt(l[z])):
            if(l[z]%k==0):
                l1[k]+=1
                l1[l[z]//k]+=1
            k+=1
        if(k==math.sqrt(l[z])):
            l1[k]+=1
        z+=1
    #print(l1)
    #print(lf)
    print(max(lf))
    t-=1