class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        start = 0
        n = len(nums)
        end = n-1

        if len(nums)==1:
            return 0


        if nums[0]>nums[1]:
            return 0

        if nums[n-1]>nums[n-2]:
            return n-1

        while start<=end:

            mid = start + (end-start)//2

            if nums[mid]>nums[mid-1] and nums[mid]>nums[mid+1]:
                return mid

            if nums[mid-1]>nums[mid]:
                end = mid-1

            elif nums[mid+1]>nums[mid]:
                start = mid+1

        
