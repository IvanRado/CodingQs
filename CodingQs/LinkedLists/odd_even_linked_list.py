from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# Straight forward solution that uses 4 pointers and a single pass 
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None: # No head
            return None
        if head.next == None or head.next.next == None:  # One or two nodes
            return head
        
        mid = head.next
        even = head.next
        odd = head
        i = 3
        
        ptr = head.next.next
        
        while ptr:
            # print(f"ptr: {ptr}")
            if i % 2 == 1:
                odd.next = ptr
                odd = ptr
            else:
                even.next = ptr
                even = ptr
                
            i += 1
            ptr = ptr.next
            
        even.next = ptr
        odd.next = mid
        return head

# A cleaner version of the same idea
class Solution2:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if (head == None):  return None
        odd = head
        even = head.next
        evenHead = even
        while even != None and even.next != None:
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next
        
        odd.next = evenHead
        return head
    

        