def fun(a):
    start = 0
    n = len(a)
    end = n-1
    
    if a[0]>a[1]:
        return 0
        
    if a[n-1]>a[n-2]:
        return n-1
        
    while start<=end:
        
        mid = start + (end-start)//2 
        
        if a[mid]>a[mid-1] and a[mid]>a[mid+1]:
            return mid 
            
        if a[mid-1]>a[mid]:
            end=mid-1 
            
        elif a[mid+1]>a[mid]:
            start = mid+1 
            
    
def bs(a, start, end, x):
    
    while start<=end:
        mid = start + (end-start)//2 
        
        if a[mid]==x:
            return mid 
            
        elif a[mid]>x:
            end=mid-1
            
        elif a[mid]<x:
            start = mid+1  
            
            
    return -1 
    
def dbs(a, start, end, x):
    
    while start<=end:
        mid = start + (end-start)//2 
        
        if a[mid]==x:
            return mid 
            
        elif a[mid]>x:
            start = mid+1  
            
            
        elif a[mid]<x:
            end=mid-1
            
            
            
    return -1 
    

    
arr = [5,10,8,7,6,5]
key = 5
idx = fun(arr)
print(idx)
print(bs(arr, 0 , idx, key))
print(dbs(arr,idx+1,len(arr)-1,key))
