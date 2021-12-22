from collections import defaultdict
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        if headA == headB:
            return headA   
        if headA == None or headB == None:
            return None
        if headA.next == None and headB.next == None:
            return None
        
        nodes = defaultdict(lambda: -1)
        
         # Do the dumb thing: store nodes of one list and check if it exists in the other
        nodeA = headA
        
        while nodeA:
            nodes[nodeA] = 1
            nodeA = nodeA.next
            
        nodeB = headB
        while nodeB:
            if nodes[nodeB] == 1:
                return nodeB
            nodeB = nodeB.next

# Same idea just using a set instead of dict
class Solution2:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        seen = set()
        itr = headA
        while itr:
            seen.add(itr)
            itr = itr.next
        itr = headB
        while itr:
            if seen.__contains__(itr):
                return itr
            itr = itr.next
        return None

# Constant memory solution and O(m+n)
class Solution3:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        def list_len(node: ListNode) -> int:
            l = 0
            while node:
                l += 1
                node = node.next
            return l
        
        len_A = list_len(headA)
        len_B = list_len(headB)
        if len_A > len_B:
            headA, headB = headB, headA
            len_A, len_B = len_B, len_A
            
        for i in range(len_B - len_A):
            headB = headB.next
            
        while headA:
            if headA == headB:
                return headA
            headA = headA.next
            headB = headB.next
            
        return None
