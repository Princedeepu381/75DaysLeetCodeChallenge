class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        
        while curr:
            nxt = curr.next  # Temporary store next node
            curr.next = prev  # Reverse the link
            prev = curr      # Move prev forward
            curr = nxt       # Move curr forward
            
        return prev