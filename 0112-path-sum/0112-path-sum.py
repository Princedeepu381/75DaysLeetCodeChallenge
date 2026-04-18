class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        
        # Check if we are at a leaf node
        if not root.left and not root.right:
            return targetSum == root.val
        
        # Recurse down with the remaining summ
        remaining_sum = targetSum - root.val
        return self.hasPathSum(root.left, remaining_sum) or self.hasPathSum(root.right, remaining_sum) 