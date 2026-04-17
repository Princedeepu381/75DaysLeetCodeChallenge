class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # Both empty
        if not p and not q:
            return True
        # One empty, or values mismatch
        if not p or not q or p.val != q.val:
            return False
        
        # Recurse
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)