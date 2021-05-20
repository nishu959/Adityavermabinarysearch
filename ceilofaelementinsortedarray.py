a = list(map(int, input().split()))
ele = int(input())


start = 0
end = len(a)-1
while(start <=end):
  mid = start + (end-start)//2
  if a[mid]==ele:
    res = ele
    break
  if a[mid]>ele:
    res = a[mid]
    end = mid - 1
   
  elif a[mid]<ele:
    start = mid +1
 
print(res)
    