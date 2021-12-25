from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Simple solution using leading and lagging pointers
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        
        if not head:
            return None
        
        lag, lead = head, head.next
        while head and head.val == val:  # Remove all instances at the start of the array
            head = head.next
            
        if not head: return head  # Return early if all the nodes have value val
        while lead:
            if lead.val == val:
                lag.next = lead.next
                lead = lead.next
            else:
                lag = lag.next
                lead = lead.next
                
        return head