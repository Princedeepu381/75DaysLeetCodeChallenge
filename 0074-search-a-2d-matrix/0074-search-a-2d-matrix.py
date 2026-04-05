class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
            
        ROWS, COLS = len(matrix), len(matrix[0])
        l, r = 0, ROWS * COLS - 1
        
        while l <= r:
            mid = l + (r - l) // 2
            
            # Translate the 1D index back into 2D row and column coordinates
            row = mid // COLS
            col = mid % COLS
            
            if matrix[row][col] > target:
                r = mid - 1
            elif matrix[row][col] < target:
                l = mid + 1
            else:
                return True
                
        return False