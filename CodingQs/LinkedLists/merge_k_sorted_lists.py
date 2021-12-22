from collections import defaultdict
from typing import List, Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Brute force approach, has O(N log N) time complexity and O(N) space complexity
# Store everything in a dictionary than reconstruct the list node
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None  
        nodes = defaultdict(lambda: 0)
        for list_i in lists:
            head = list_i
            while head:
                nodes[head.val] += 1
                head = head.next
        
        
        # Now the dictionary has all the values
        sorted_keys = sorted(nodes.keys())
        print(sorted_keys)
        
        if not sorted_keys:
            return None
        
        head = ListNode(val = sorted_keys[0], next=None)
        node = head
        nodes[sorted_keys[0]] -= 1
        for key in sorted_keys:
            repeats, val = nodes[key], key
            for i in range(repeats):
                new_node = ListNode(val=val, next=None)
                node.next = new_node
                node = new_node
                
        return head

from queue import PriorityQueue

# https://stackoverflow.com/questions/40205223/priority-queue-with-tuples-and-dicts
class use_only_first:
    def __init__(self, first, second):
        self._first, self._second = first, second

    def __lt__(self, other):
        return self._first < other._first

# Alternative solution:
# Compare every k nodes (head of every linked list) and get the node with the smallest value.
# Extend the final sorted linked list with the selected nodes.
# Use a priority queue to speed up
# Time: O(N log k), Space: O(n) + O(k)
class Solution2:
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        q = PriorityQueue()
        for l in lists:
            if l:
                q.put(use_only_first(l.val, l))
        head = point = ListNode(0)
        while not q.empty():    # PriorityQueue has no len()
            use_object = q.get()
            val = use_object._first
            node = use_object._second
            point.next = ListNode(val)
            point = point.next
            node = node.next
            if node:
                q.put(use_only_first(node.val, node))
        return head.next

# Another approach: divide and conquer
# Combine pairs of linked lists into pairs and sort each pair
# Keep repeating until a single linked list is left
# Time: O (N log k), Space: O(1) - we can merge two lists in place

class Solution3(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        amount = len(lists)
        interval = 1
        while interval < amount:
            for i in range(0, amount - interval, interval * 2):
                lists[i] = self.merge2Lists(lists[i], lists[i + interval])
            interval *= 2
        return lists[0] if amount > 0 else None

    def merge2Lists(self, l1, l2):
        head = point = ListNode(0)
        while l1 and l2:
            if l1.val <= l2.val:
                point.next = l1
                l1 = l1.next
            else:
                point.next = l2
                l2 = l1
                l1 = point.next.next
            point = point.next
        if not l1:
            point.next=l2
        else:
            point.next=l1
        return head.next