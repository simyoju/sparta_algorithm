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

    def get_kth_node_from_last(self, k):
        # 구현해보세요!
        num_of_list = 1
        cur = self.head
        while cur.next is not None:
            num_of_list += 1
            cur = cur.next
        print(num_of_list)

        index = num_of_list - k
        cnt = 0
        cur = self.head
        if index < 0:
            print("범위를 벗어나 head의 값을 출력합니다")
        while cnt < index:
            cnt += 1
            cur = cur.next
            # print(index)
        return cur


linked_list = LinkedList(6)
linked_list.append(7)
linked_list.append(8)
linked_list.append(9)

print(linked_list.get_kth_node_from_last(5).data)  # 7이 나와야 합니다!