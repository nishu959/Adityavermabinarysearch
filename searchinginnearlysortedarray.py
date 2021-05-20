a = list(map(int, input().split()))
ele = int(input())


start = 0
end = len(a)-1
p =-1
while (start<=end):
  mid = start + (end-start)//2
  if a[mid]==ele:
    p=mid
    break 
  if mid-1>=start and a[mid-1]==ele:
    p=mid-1
    break
  if mid+1<=end and a[mid+1]==ele:
    p=mid+1
    break
   
  if ele<=a[mid]:
    end = mid - 2
   
  if ele>=a[mid]:
    start = mid +2
   

print(p)