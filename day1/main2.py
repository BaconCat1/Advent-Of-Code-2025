import os
p=50;z=0
here=os.path.dirname(__file__)
for s in open(os.path.join(here,"input.txt")):
    d=int(s[1:])
    k=(-p)%100 or 100 if s[0]=="R" else p%100 or 100
    if k<=d:z+=1+(d-k)//100
    p=(p+(-d if s[0]=="L" else d))%100
print(z)
