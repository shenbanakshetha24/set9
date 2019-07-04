dn=input()
fo=[]
for i in dn:
 if(i.isnumeric()):
  fo.append(i)
print("".join(fo))
