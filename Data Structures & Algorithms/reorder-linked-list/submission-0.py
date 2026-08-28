# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #splitting the list
        point = head
        node = []
        while point:
            node.append(point)
            point = point.next
        i = 0
        j = len(node)-1
        h=i+j//2
        while i<j:
            node[i].next = node[j]
            i += 1
            node[j].next = node[i]
            j -= 1
        node[i].next = None
