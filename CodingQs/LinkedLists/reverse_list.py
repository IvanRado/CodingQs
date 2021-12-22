from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return None
        if head.next == None:
            return head
        
        new_head = head
        head = head.next
        new_head.next = None
        while head:
            tmp = head.next
            head.next = new_head
            new_head = head
            head = tmp
            