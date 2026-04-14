class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        
        # Swap the children
        root.left, root.right = root.right, root.left
        
        # Recurse
        self.invertTree(root.left)
        self.invertTree(root.right)
        
        return root