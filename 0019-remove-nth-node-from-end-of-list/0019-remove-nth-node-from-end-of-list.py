class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        fast = slow = dummy
        
        # Advance fast pointer so that there is a gap of n nodes between fast and slow
        for _ in range(n):
            fast = fast.next
            
        # Move fast to the end, maintaining the gap
        while fast.next:
            fast = fast.next
            slow = slow.next
            
        # Skip the nth node from the end
        slow.next = slow.next.next
        
        return dummy.next