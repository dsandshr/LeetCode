# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def recReverseList(self, head: ListNode) -> ListNode:      # recursive reverseList
        if head == None or head.next == None: return head
        new_list = self.recReverseList(head.next)
        head.next.next = head
        head.next = None
        return new_list
    
    def iterRecursiveList(self, head: ListNode) -> ListNode:
        prev = None
        curr = head
        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
        return prev