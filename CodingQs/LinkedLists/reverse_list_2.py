from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# A fairly straightforward solution using only pointers
# Reverses the list in a single pass
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if head.next == None: 
            return head
        if left == right:
            return head
    
        i = 1
        lag, lead = head, head.next
        
        if left == 1:
            anchor = head
        else:
            anchor = None
        
        
        while lag:
            if i == left - 1:
                anchor = lag
            if i >= left and i < right:
                tmp = lead.next
                lead.next = lag
                lag = lead
                lead = tmp
            elif i == right:
                if left != 1:
                    anchor.next.next = lead
                    anchor.next = lag
                else:
                    anchor.next = lead
                    anchor = lag
                break
            else:
                lead = lead.next
                lag = lag.next
                
            i += 1
        
        if left == 1:
            return anchor
        else:
            return head

# A recursive solution
class Solution2:
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """

        if not head:
            return None

        left, right = head, head
        stop = False
        def recurseAndReverse(right, m, n):
            nonlocal left, stop

            # base case. Don't proceed any further
            if n == 1:
                return

            # Keep moving the right pointer one step forward until (n == 1)
            right = right.next

            # Keep moving left pointer to the right until we reach the proper node
            # from where the reversal is to start.
            if m > 1:
                left = left.next

            # Recurse with m and n reduced.
            recurseAndReverse(right, m - 1, n - 1)

            # In case both the pointers cross each other or become equal, we
            # stop i.e. don't swap data any further. We are done reversing at this
            # point.
            if left == right or right.next == left:
                stop = True

            # Until the boolean stop is false, swap data between the two pointers     
            if not stop:
                left.val, right.val = right.val, left.val

                # Move left one step to the right.
                # The right pointer moves one step back via backtracking.
                left = left.next           

        recurseAndReverse(right, m, n)
        return head