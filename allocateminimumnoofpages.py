a = list(map(int,input().split()))

k = int(input())

def isvalid(a, mid, k):
  if len(a)<k:
    return -1
  student = 1
  s =0
  for i in a:
    s = s+i
    if s>mid:
      student += 1
      s = i
    if student>k:
      return False
  return True
      



start = max(a)
end = sum(a)-min(a)

while(start<=end):
  mid = start + (end-start)//2
  if isvalid(a, mid, k)==True:
    res = mid
    end = mid-1
  
  elif isvalid(a, mid, k)==False:
    start = mid +1
 
print(res)