a = list(map(int, input().split()))

start = 0
end = 1
while a[end]<1:
  start = end
  end = end*2

res = -1
while(start<=end):
  mid = start + (end-start)//2
  if a[mid]==1:
    res = mid
    end = mid - 1
  if a[mid]<1:
    start = mid+1
  
  
print(res)
    