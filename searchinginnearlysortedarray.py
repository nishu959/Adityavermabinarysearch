a = [10, 3, 40, 20, 50, 80, 70]
x = 40



def fun(a, x):
    start = 0
    end = len(a)-1

    while start<= end:
        mid = start + (end-start)//2
        
        if a[mid] == x:
            return mid
            
        if mid-1>=start and a[mid-1]==x:
            return mid-1
            
        if mid+1<=end and a[mid+1]==x:
            return  mid+1
            
        if x > a[mid]:
            start = mid + 2
            
        if x< a[mid]:
            end= mid-2
            
    return -1
            
print(fun(a, x))
        
