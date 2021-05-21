a = list(map(str, input().split()))
key = input()

start = 0
ans = "*"
end = len(a)-1

while(start <=end):
  mid = start + (end-start)//2
  if a[mid]==key:
    start = mid +1
  if a[mid]> key:
    ans = a[mid]
    end = mid - 1
  if a[mid]<key:
    start = mid +1
  
    
    
print(ans)
