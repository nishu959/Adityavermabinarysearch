a = list(map(int, input().split()))
ele = int(input())

start = 0
end = len(a) - 1
ans = -1

while start<=end:
  mid = start + (end-start)//2
  if a[mid]==ele:
    ans = mid 
    end= mid - 1
  elif ele < a[mid]:
    end  = mid - 1
  else:
    start = mid + 1
    
    

print(ans)


#for last occurance
# in a[mid]==ele just change start = mid +1