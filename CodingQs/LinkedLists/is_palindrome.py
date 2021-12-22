from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        vals = []
        
        while head:
            vals.append(head.val)
            head = head.next
            
            
        l, r = 0, len(vals) - 1
        
        while l < r:
            if vals[l] != vals[r]: return False
            l += 1
            r -= 1
            
        return True
        
class Solution2:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # Use fast and slow pointers to get to the midpoint of the list
        fast, slow = head, head

        # Find the midpoint of the list
        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next

        # Reverse the second half
        prev, next_ = None, None

        # Moving from the middle 
        while slow:
            next_ = slow.next
            slow.next = prev
            prev = slow
            slow = next_

        # So we need two pointers
        left, right = head, prev

        # Traverse in the rever direction
        while right:
            if left.val != right.val:
                return False
            else:
                right = right.next
                left = left.next

        return True
