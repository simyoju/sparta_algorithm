# [3] -> [4]
# data, next
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

node = Node(3)
first_node = Node(4)
node.next = first_node
print(node.data)
print(node.next.data)

class LinkedList:
    def __init__(self, data):
        self.head = Node(data)

    def append(self, data):
        #self.head.next = Node(data) # 이렇게 하면 안됨. 맨 뒤에 붙는 게 아니라 헤드 뒤에 붙게 되는 것이니까
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next =Node(data)
        print(cur.data)

    def print_all(self):
        print("start")
        cur = self.head
        while cur is not None:
            print(cur.data)
            cur = cur.next

linked_list = LinkedList(6)
linked_list.append(7)
linked_list.append(8)
linked_list.print_all()
# print(linked_list.head.next)