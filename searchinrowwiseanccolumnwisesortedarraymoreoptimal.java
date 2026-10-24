class Solution {
    public boolean searchMatrix(int[][] matrix, int target) {

        if(matrix==null){
            return false;
        }

        int m = matrix.length;
        int n = matrix[0].length;

        if ( m == 0 || n == 0) {
            return false;
        }
        int start = 0;
        int end = m * n-1;
        
        while(start <= end){
            int mid = start + (end-start)/2;
            int row = mid / n;
            int col = mid % n;

            

            if(matrix[row][col]==target){
                return true;
            }  

            if(matrix[row][col] > target){
                end = mid-1;
            } else {
                start = mid + 1;
            }

        }

        return false;



       
        
    }
}
