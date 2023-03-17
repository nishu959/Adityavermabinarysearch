a =[2, 5, 10, 12, 15]
target = 7


def fun(a, x):
    
    
    
    start = 0 
    end = len(a)-1 
    
    if x>a[end]:
        return a[end]
        
    if x<a[start]:
        return a[start]
    
    while start<= end:
        mid = start + (end-start)//2 
        
        if a[mid]==x:
            return x 
            
        if a[mid]>x:
            end = mid-1
            
        elif a[mid]<x:
            start = mid + 1  
            
            
    start_diff = abs(a[start]-x)
    end_diff = abs(a[end]-x)
    
    if start_diff < end_diff:
        return a[start]
    elif start_diff>=end_diff:
        return a[end]
        
        
print(fun(a, target))
            

