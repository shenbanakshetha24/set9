g1,s1=map(int,input().split())
maxima=max(g1,s1)
while(1):
 if(maxima%g1==0 and maxima%s1==0):
  print(maxima)
  break
 maxima+=1
