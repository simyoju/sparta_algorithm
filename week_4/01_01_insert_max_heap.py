class MaxHeap:
    def __init__(self):
        self.items = [None]

    def insert(self, value):
        # 구현해보세요!
        # 1. 맨 마지막에 삽입한다
        # 2. 부모노드와 비교하고 value가 더 크면 자리를 바꾼다
        # 3. 부모노드보다 작거나 가장 위에 도달하지 않을 때까지 2과정을 반복한다.
        self.items.append(value)
        cur_index = len(self.items)-1

        while cur_index > 1:
            parent_index = cur_index // 2
            if self.items[parent_index] < self.items[cur_index]:
                self.items[parent_index], self.items[cur_index] = self.items[cur_index], self.items[parent_index]
                cur_index = parent_index
            else:
                break
        return


max_heap = MaxHeap()
max_heap.insert(3)
max_heap.insert(4)
max_heap.insert(2)
max_heap.insert(9)
print(max_heap.items)  # [None, 9, 4, 2, 3] 가 출력되어야 합니다!