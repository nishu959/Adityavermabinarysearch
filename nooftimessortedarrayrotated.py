a = list(map(int, input().split()))


start = 0
end = len(a) - 1
ans = -1
n = len(a)-1

while (start<=end):
  
  if a[start] <= a[end]:
    ans =start
    #print(ans)
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
  
#for right rotation
print(ans)

#for left rotation
print(len(a)-ans)

