def minele(a):
  start = 0
  end = len(a) - 1
  ans = -1
  n = len(a)-1
  while (start<=end):
    if a[start] <= a[end]:
      ans =start
      break
    
    mid = (start + end)//2
    pre = (mid +n - 1) % n
    nex = (mid + 1) % n
  
    if a[mid]<=a[nex] and a[mid]<=a[pre] :
      ans = mid
      break
    if a[start] <=a[mid]:
      start = mid + 1
    
    elif a[mid] <=a[end]:
      end = mid - 1
 
  return ans

def bs(a, start, end, ele):
  while(start <= end):
    mid = start + (end-start)//2
    if a[mid]==ele:
      return mid
    elif ele>=a[mid]:
      start = mid +1
    elif ele<=a[mid]:
      end = mid - 1
  return -1
      
a = list(map(int, input().split()))
ele = int(input())
index =minele(a)


p = bs(a, 0,index-1, ele)
q = bs(a, index, len(a)-1, ele)

if p!=-1:
  print(p)
  
if q!=-1:
  print(q)
  
if p==-1 and q==-1:
  print("ele not found")

