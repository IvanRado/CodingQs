from typing import tuple, Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return None
        if head.next == None:
            return head
        
        def list_size(head: ListNode) -> tuple[int, ListNode]:
            i = 0
            last = None
            while head:
                i += 1
                last = head
                head = head.next               
            return i, last
        
        # Get the list len
        list_len, last = list_size(head)
        rotations = k % list_len  # Get effective rotation spots
        
        lag, lead = head, head.next
        for i in range(1, list_len):
            if i == list_len-rotations:  # We are at the node where we need to rearrange connections
                lag.next = None
                last.next = head
                head = lead
                break
            else:
                lag = lag.next
                lead = lead.next
                
        return head
            