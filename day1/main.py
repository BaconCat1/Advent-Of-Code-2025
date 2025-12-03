p=50;c=0
for s in open("input.txt"):
    d=int(s[1:]);p=(p-d if s[0]=='L' else p+d)%100;c+=p==0
print(c)
