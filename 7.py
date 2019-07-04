h3,h4=map(int,input().split())
m=1
while(m<=h3 and m<=h4):
 if(h3%m==0 and h4%m==0):
  gcd=m
 m=m+1
print(gcd)
