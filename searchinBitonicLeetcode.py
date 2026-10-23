# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
# class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        idx_max = self.fun(mountain_arr)
        if target == mountain_arr.get(idx_max):
            return idx_max
        
        n = mountain_arr.length()

        bs = self.bs(mountain_arr, 0, idx_max, target)
        if bs != -1:
            return bs

        bsr = self.bsr(mountain_arr, idx_max + 1, n - 1, target)
        if bsr != -1:
            return bsr

        return -1

    def bs(self, arr: 'MountainArray', start: int, end: int, tar: int) -> int:
        while start <= end:
            mid = start + (end - start) // 2

            val = arr.get(mid)
            if val == tar:
                return mid
            if tar > val:
                start = mid + 1
            else:
                end = mid - 1

        return -1

    def bsr(self, arr: 'MountainArray', start: int, end: int, tar: int) -> int:
        while start <= end:
            mid = start + (end - start) // 2

            val = arr.get(mid)
            if val == tar:
                return mid
            if tar > val:
                end = mid - 1
            else:
                start = mid + 1

        return -1

    def fun(self, arr: 'MountainArray') -> int:
        # Same as peak element 162. Find Peak Element leetcode
        n = arr.length()

        if n == 1:
            return 0

        if arr.get(0) > arr.get(1):
            return 0

        if arr.get(n - 1) > arr.get(n - 1):
            return n - 1

        start = 1
        end = n - 2

        while start <= end:
            mid = start + (end - start) // 2
            val = arr.get(mid)
            val2 = arr.get(mid - 1)

            if (val > val2) and (val > arr.get(mid + 1)):
                return mid

            if val2 > val:
                end = mid - 1
            else:
                start = mid + 1

        return -1
