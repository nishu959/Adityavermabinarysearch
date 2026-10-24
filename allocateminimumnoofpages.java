class Solution {
    public int findPages(int[] arr, int k) {
        // code here
        long max = arr[0];
        int n = arr.length;
        
        if(k>n){
            return -1;
        }
        
        long s = arr[0];
        for(int i=1; i<n;i++){
            max = Math.max(max, arr[i]);
            s += arr[i];
        }
        
        long start = max;
        long end = s;
        long ans = -1;
        
        while(start<=end){
            long mid = start + (end-start)/2;
            if(isPossible(arr, mid, k)){
                ans= mid;
                end = mid-1;
            } else {
                start = mid +1;
            }
            
        }
        
        return (int) ans;
        
    }
    
    private boolean isPossible(int[] arr, long mid, int k){
        int count =1;
        long s = 0;
        int n = arr.length;
        
        for(int i=0;i<n;i++){
            if(s+arr[i] > mid){
                count += 1;
                s = arr[i];
                if(count > k){
                    return false;
                }
            } 
             else {
                s += arr[i];
                
            }
        }
        
        return true;
        
        
        
    }
}
