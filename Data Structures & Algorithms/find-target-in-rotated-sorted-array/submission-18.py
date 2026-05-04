class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start, end = 0, len(nums)-1 

        while start+1 < end:
            mid = (start + end)//2
            if nums[mid]>=nums[start]:
                if nums[start] <= target <= nums[mid]:
                    end = mid
                else:
                    start = mid
            elif nums[mid]<nums[start]:
                if nums[mid] <= target < nums[start]:
                    start = mid 
                else:
                    end = mid 
        
        if nums[start] == target:
            return start
        elif nums[end] == target:
            return end 
        else:
            return -1 
                

        