# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from Linked_List import Node, LinkedList


class Solution:
    def reverseList(self, head: Node) -> Node:
        if head:
            prevNode = None
            current = head

            while current:
                nextNode = current.next
                current.next = prevNode
                prevNode = current
                current = nextNode

            return prevNode
