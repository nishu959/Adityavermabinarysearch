a = list(map(int, input().split()))

start = 0
end = len(a)-1


while( start<=end):
  mid = start + (end-start)//2
  if len(a)==1:
    print(0)
    break
  if mid>0 and mid<len(a)-1:
    if a[mid]>a[mid-1] and a[mid]>a[mid+1]:
      print(mid) 
      break
    elif a[mid-1]>a[mid]:
      end = mid-1
    else:
      start = mid+1
      
  elif mid==0:
    if a[0]>a[1]:
      print(0) 
      break
    else:
      print(1)
      break
  elif mid==len(a)-1:
    if a[len(a)-1]>a[len(a)-2]:
      print(len(a)-1) 
      break
    else:
      print(len(a)-2) 
      break