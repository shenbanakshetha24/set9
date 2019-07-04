gf=list(input())
h=[]
for i in gf:
 if i not in h:
  h.append(i)
if(gf==h):
 print("Yes")
else:
 print("No")
