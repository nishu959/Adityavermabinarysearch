a = list(map(int, input().split()))

ele = int(input())

start =0
end = len(a)-1
ans = -1
while(start<=end):
  mid = start + (end-start)//2
  if a[mid]==ele:
    ans = ele
    break
  if a[mid]>ele:
    end = mid - 1
  if a[mid]<ele:
    start = mid +1
  
    
p=abs(a[end]-ele)
q =abs(a[start]-ele)


if ans!=-1:
  print(ans)
elif p<=q:
  print(a[end])
else:
  print(a[start])