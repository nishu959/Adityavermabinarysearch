a = list(map(int, input().split()))
ele = int(input())


start = 0
end = len(a)-1


while(start<=end):
  mid = start + (end-start)//2
  if a[mid]==ele:
    res =a[mid]
    break
  if ele<a[mid]:
    end = mid - 1
   
  elif ele>a[mid]:
    res = a[mid]
    start = mid +1
   
  
print(res)