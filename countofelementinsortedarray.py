
def firstoccurance(a, ele):
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
  return ans


def lastoccurance(a, ele):
  start = 0
  end = len(a) - 1
  ans = -1

  while start<=end:
    mid = start + (end-start)//2
    if a[mid]==ele:
      ans = mid 
      start = mid +1
    elif ele < a[mid]:
      end  = mid - 1
    else:
      start = mid + 1
  return ans



a = list(map(int, input().split()))
ele = int(input())

lo = lastoccurance(a, ele)
fo = firstoccurance(a, ele)


print(lo - fo +1)