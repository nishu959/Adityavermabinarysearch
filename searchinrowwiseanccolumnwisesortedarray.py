n = int(input())
m= int(input())
a = []

for i in range(n):
  a.append(list(map(int,input().split())))
  
  
key = int(input())


i =0
j =m-1

def rwcw(a, i, j, key):
  n = len(a)
  m = len(a[0])
  while(i>=0 and i<n and j >=0 and j <m):
    if a[i][j]==key:
      return [i, j] 
    elif a[i][j]>key:
      j -= 1
    elif a[i][j]<key:
      i += 1
  return -1
 
 
print(rwcw(a, i, j, key))
 