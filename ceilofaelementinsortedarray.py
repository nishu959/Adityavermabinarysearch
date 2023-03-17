
def ceilingInSortedArray(n, x, arr):
    # Write your code here.
    start = 0
    end = n-1
    ans = -1
    while start <= end:
        mid = start+ (end-start)//2

        if arr[mid]==x:
            return x 

        if arr[mid]>x:
            ans = arr[mid] 
            end = mid-1

        elif arr[mid]<x:
            start = mid + 1

    return ans
