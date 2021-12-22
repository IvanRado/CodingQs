from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: return None
        if head.next == None:
            return head
        
        vals = [head.val]
        node = head.next
        last = head
        
        while node:
            val = node.val
            if val in vals:
                last.next = node.next
                node = node.next
            else:
                vals.append(val)
                last = node
                node = node.next
                
        return head
        