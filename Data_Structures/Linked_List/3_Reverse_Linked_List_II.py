# Link: https://leetcode.com/problems/reverse-linked-list-ii/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from Linked_List import Node


class Solution:
    def reverseBetween(self, head: Node, m: int, n: int) -> Node:
        '''
        :param head: the starting point of the list
        :param m: starting position to reverse
        :param n: ending position to reverse
        :return: the head of the list
        Note: 1 ≤ m ≤ n ≤ length of list.
        Input: 1->2->3->4->5->NULL, m = 2, n = 4
        Output: 1->4->3->2->5->NULL
        '''

        # TODO: determine if the starting node is the head of the list or not
        # m_node: the node which the reversing processing begins
        if m > 1:
            starting_point = head
            for _ in range(1, m - 1):  # why m-1?
                starting_point = starting_point.next
            m_node = starting_point.next
        else:
            starting_point = None
            m_node = head

        # reverse the desired part
        current = m_node
        prev_node = starting_point
        for _ in range(m, n + 1):
            next_node = current.next
            current.next = prev_node
            prev_node = current
            current = next_node

        # link back the node. example: 1 -> 2 -> 3 -> 4
        # reverse 2 -> 3
        # then after reversing, 1 is connected to 3
        if current:
            m_node.next = current
        else:
            m_node.next = None

        # return the starting point based on the value of m,
        #   which means based on whether the head is reversed or not
        if m > 1:
            starting_point.next = prev_node
            return head
        else:
            return prev_node

    def print_list(self, head):
        if head:
            current = head
            print(current.val, end="->")
            while current.next:
                current = current.next
                print(current.val, end="->")


if __name__ == '__main__':
    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(3)
    n4 = Node(4)
    n5 = Node(5)
    n1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n5

    s = Solution()
    # s.print_list(n1)

    try:
        s.print_list(s.reverseBetween(n1, 2, 4))
    except Exception as exc:
        print(exc)
    # s.reverseBetween(n1, 2, 4)
