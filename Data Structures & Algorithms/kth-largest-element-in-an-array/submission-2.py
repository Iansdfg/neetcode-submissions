class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return self.quick_select(len(nums)-k, nums, 0, len(nums)-1)


    def quick_select(self, k, nums, start, end):
        left, right = start, end
        pivot = nums[(left + right)//2]
        while left <= right:
            while left <= right and nums[left] < pivot:
                left += 1 
            while left <= right and nums[right] > pivot: 
                right -= 1 
            if left <= right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1 
                right -= 1 
            
        if k >= left:
            return self.quick_select(k, nums, left, end)
        elif k <= right:
            return self.quick_select(k, nums, start, right)
        else:
            return nums[k]

        