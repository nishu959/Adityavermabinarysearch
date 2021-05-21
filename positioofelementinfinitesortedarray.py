a = list(map(int, input().split()))
key = int(input())

start = 0
end = 1
while(key >a[end]):
  start = end
  end = end *2
 
ans = -1
while start<=end:
  mid = start + (end-start)//2
  if a[mid]==key:
    ans = mid
    break
  if a[mid]>key:
    end = mid - 1
  elif a[mid]<key:
    start = mid +1
    
    
print(ans)

