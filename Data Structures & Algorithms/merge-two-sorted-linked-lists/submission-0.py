# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        list3: Optional[ListNode]
        curr1 = list1
        curr2 = list2

        while curr1.next != None and curr2.next!= None:

            if curr1 <= curr2:
                list3.val = curr1.val
                list3 = list3.next
                curr1 = curr1.next
            else:
                list3.cal = curr2.val
                list3 = list3.next
                curr2 = curr2.next
            
            
        return list3

        