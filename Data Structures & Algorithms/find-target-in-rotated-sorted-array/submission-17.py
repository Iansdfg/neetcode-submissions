class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start, end = 0, len(nums)-1 
        while start + 1 < end:
            mid = (start + end)//2
            print(mid, nums[mid])
            if nums[start] <= nums[mid]:
                if nums[start] <= target < nums[mid]:
                    end = mid 
                else:
                    start = mid
            elif nums[start] > nums[mid]:
                if nums[mid] < target <= nums[end]:
                    start = mid 
                else:
                    end = mid
        if nums[end] == target:
            return end
        elif nums[start] == target:
            return start
        else:
            return -1 


            
                