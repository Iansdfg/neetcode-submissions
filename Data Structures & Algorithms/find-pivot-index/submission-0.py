class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        sum_right = 0
        sum_list_right = []
        for left in range(len(nums)):
            right = len(nums)-1-left
            sum_right += nums[right]
            sum_list_right.append(sum_right)
        sum_list_right.reverse()
        sum_left = 0
        for left in range(len(nums)):
            sum_left += nums[left]
            print(sum_left)
            if sum_left == sum_list_right[left]:
                return left

        return -1