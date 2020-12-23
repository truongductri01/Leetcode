class Node(object):
    def __init__(self, val):
        self.val = val
        self.next = None


class LinkedList(object):
    def __init__(self, head=None):
        self.head = head

    def append(self, new_node: Node):
        if self.head:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        else:
            self.head = new_node

    def print(self):
        if self.head:
            current = self.head
            print(current.val, end=" -> ")
            while current.next:
                current = current.next
                print(current.val, end=" -> ")
        else:
            print("Empty Linked List")

    @staticmethod
    def generate(array_of_values):
        head = Node(array_of_values[0])
        linked_list = LinkedList(head)

        for i in range(1, len(array_of_values)):
            node = Node(array_of_values[i])
            linked_list.append(node)

        return linked_list


if __name__ == '__main__':
    ll = LinkedList.generate([1, 2, 3])

    ll.print()
