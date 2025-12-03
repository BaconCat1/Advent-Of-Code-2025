import os

r=[tuple(map(int,t.split('-')))
   for t in open(os.path.join(os.path.dirname(__file__),"input.txt"))
   .read().split(',') if t]

m=max(b for _,b in r);ans=0
for k in range(1,len(str(m))//2+1):
    L=10**k; start=10**(k-1); end=min(L-1,m//(L+1))
    for x in range(start,end+1):
        v=x*(L+1)          #Num tt where t has k digits
        if any(a<=v<=b for a,b in r): ans+=v

print(ans)
