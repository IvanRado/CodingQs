from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None and list2 is not None:
            return list2  # Return only second list if first is None
        elif list1 is not None and list2 is None:
            return list1  # Return only first list if second is None
        elif list1 is None and list2 is None:
            return None  # Return None if both are None
        
        if list1.val < list2.val:
            head = list1
            list1 = list1.next
        else: 
            head = list2
            list2 = list2.next
        
        node = head
        i = 0
        while list1 is not None and list2 is not None:
            
            if list1.val < list2.val:
                node.next = list1
                node = list1
                list1 = list1.next
            else:
                node.next= list2
                node = list2
                list2 = list2.next
                
            i+= 1
                
        if list1 is None:
            node.next = list2
        elif list2 is None:
            node.next = list1
                
                
        return head


# Cleaner solution
class Solution2:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 and list2:
            if list1.val > list2.val:
                list1, list2 = list2, list1
            
            list1.next = self.mergeTwoLists(list1.next, list2)

        return list1 or list2
        
    
                