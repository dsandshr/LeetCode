# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        
        new_list = ListNode(0)
        buf = new_list
        
        while l1 or l2:
            if (l1 and l2 and l1.val <= l2.val) or (l1 and l2 == None):
                new_list.val = l1.val
                l1 = l1.next
            elif (l2 and l1 and l2.val < l1.val) or (l2 and l1 == None):
                new_list.val = l2.val
                l2 = l2.next
            
            if l1 or l2:
                new_list.next = ListNode(0)
                new_list = new_list.next
        
        return buf