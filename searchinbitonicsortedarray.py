def peak(a,start, end):
  while( start<=end):
    mid = start + (end-start)//2
    if len(a)==1:
      return 0
  
    if mid>0 and mid<len(a)-1:
      if a[mid]>a[mid-1] and a[mid]>a[mid+1]:
        return mid
     
      elif a[mid-1]>a[mid]:
        end = mid-1
      else:
        start = mid+1
      
    elif mid==0:
      if a[0]>a[1]:
        return 0
      
      else:
        return 1
     
    elif mid==len(a)-1:
      if a[len(a)-1]>a[len(a)-2]:
        return (len(a)-1) 
     
      else:
        return (len(a)-2) 
        
def bsa(a, start, end, ele):
  while(start<=end):
    mid = start + (end-start)//2
    if a[mid]==ele:
      return mid
    elif a[mid]>ele:
      end = mid-1
    elif a[mid]<ele:
      start = mid+1
      
  return -1
  
def bsd(a, start, end, ele):
  while(start<=end):
    mid = start + (end-start)//2
    if a[mid]==ele:
      return mid
    elif a[mid]>ele:
      start = mid +1
    elif a[mid]<ele:
      end = mid-1
  return -1
  
  
  
a = list(map(int, input().split()))
ele = int(input())
start = 0
end = len(a)-1   
index = peak(a, start, end)

p = bsa(a, 0,index-1,ele )
q = bsd(a, index, len(a)-1,ele)

if p==-1 and q==-1:
  print(-1)
elif p!=-1:
  print(p)
elif q!=-1:
  print(q)



