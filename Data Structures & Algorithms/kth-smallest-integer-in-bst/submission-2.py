# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        dummy = TreeNode(-1)
        dummy.right = root
        stack = [dummy]

        for _ in range(k+1):
            curr = stack.pop()
            res = curr.val

            if curr.right:
                stack.append(curr.right)
                curr = curr.right

                while curr.left:
                    stack.append(curr.left)
                    curr = curr.left

        return res