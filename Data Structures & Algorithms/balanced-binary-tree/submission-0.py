# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        left_height = self.dfs(root.left, 0)
        rigth_height = self.dfs(root.right, 0)

        if left_height > rigth_height:
            diff = left_height - rigth_height
        else:
            diff = rigth_height - left_height

        return diff <= 1

    def dfs(self, root: Optional[TreeNode], h: int) -> int:
        if not root: return h
        
        left_height = self.dfs(root.left, h + 1)
        rigth_height = self.dfs(root.right, h + 1)

        return max(left_height, rigth_height)