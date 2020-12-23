from Linked_List import Node, LinkedList


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Node) -> bool:
        # using fast and slow pointer: need more explanation on this
        if head is None or head.next is None:
            return False

        fast = head
        slow = head

        while slow and fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True

        return False
