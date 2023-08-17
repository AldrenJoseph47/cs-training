m=[]
count=0
for i in range(len(m)):
  if a[i]!=0 :
    m.append(a[i])
  else:
    count=count+1
for i in range(count):
  m.append(0)
for i in range(m):
  print(m[i],end=' ')
