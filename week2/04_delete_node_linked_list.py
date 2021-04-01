class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self, value):
        self.head = Node(value)

    def append(self, value):
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = Node(value)

    def print_all(self):
        cur = self.head
        while cur is not None:
            print(cur.data)
            cur = cur.next

    def get_node(self, index):
        cnt = 0
        cur = self.head
        while cnt is not index:
            cnt += 1
            cur = cur.next
        print(cur.data)
        return "index 번째 노드를 반환해보세요!"

    def add_node(self, index, value):
        cnt = 0
        cur = self.head
        nd = Node(value)
        while cnt < index:
            cnt += 1
            cur = cur.next
        nxt = cur.next
        cur.next = nd
        nd.next = nxt
        return "추가 완료"

    def delete_node(self, index):
        cnt = 0
        cur = self.head
        if index == 0:
            self.head = cur.next
        else:
            while cnt < index:
                cnt += 1
                befo = cur
                cur = cur.next
            befo.next = cur.next

linked_list = LinkedList(5)
linked_list.append(12)
linked_list.append(13)
linked_list.append(14)
linked_list.add_node(0, 15)
linked_list.delete_node(0)
linked_list.print_all()

