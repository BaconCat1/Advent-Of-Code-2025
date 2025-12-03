import os

R=[tuple(map(int,t.split('-')))
   for t in open(os.path.join(os.path.dirname(__file__),"input.txt"))
   .read().split(',') if t]

M=max(b for _,b in R); seen=set(); ans=0
for k in range(1,len(str(M))):
    p=10**k
    for n in range(2,len(str(M))//k+1):
        f=(10**(k*n)-1)//(p-1)        #1 + 10^k + ... + 10^(k(n-1))
        lo=10**(k-1); hi=min(p-1,M//f)
        if lo>hi: break
        for x in range(lo,hi+1):
            v=x*f
            if v not in seen and any(a<=v<=b for a,b in R):
                seen.add(v); ans+=v

print(ans)
#EZ