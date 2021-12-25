from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Straightforward solution using fast and slow pointers
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head.next: # One node, return head
            return head
        if not head.next.next: # Two nodes, return the second
            return head.next
        
        fast, slow = head.next, head
        
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            
        if fast:
            return slow.next
        else:
            return slow