class MaxHeap:
    def __init__(self):
        self.items = [None]

    def insert(self, value):
        self.items.append(value)
        cur_index = len(self.items) - 1

        while cur_index > 1:  # cur_index 가 1이 되면 정상을 찍은거라 다른 것과 비교 안하셔도 됩니다!
            parent_index = cur_index // 2
            if self.items[parent_index] < self.items[cur_index]:
                self.items[parent_index], self.items[cur_index] = self.items[cur_index], self.items[parent_index]
                cur_index = parent_index
            else:
                break

    def delete(self):
        # 구현해보세요!
        # 1. 루트랑 맨 마지막 원소 교환
        # 2. 마지막 원소(원 루트) 삭제 - 저장해놔야함 리턴해야해서
        # 3. 변경된 루트노드와 자식들을 비교
        # 4. 자식이 더 크다면 교환
        # 5. 자식들이 더 작거나 바닥레벨까지 오면 멈춤
        # 6. 2번에 저장한 값 반환

        # ! 마지막 원소: len(items)-1에 있음!
        self.items[1], self.items[len(self.items)-1] = self.items[len(self.items)-1], self.items[1]
        root_data = self.items.pop()

        cur_index = 1
        while cur_index * 2 < len(self.items) - 1:
            left_child_idx = cur_index * 2
            right_child_idx = cur_index * 2 + 1
            if self.items[cur_index] < self.items[left_child_idx]:
                self.items[cur_index], self.items[left_child_idx] = self.items[left_child_idx], self.items[cur_index]
                cur_index = left_child_idx
            elif self.items[cur_index] < self.items[right_child_idx]:
                self.items[cur_index], self.items[right_child_idx] = self.items[right_child_idx], self.items[cur_index]
                cur_index = right_child_idx
            else:
                break
        return root_data


max_heap = MaxHeap()
max_heap.insert(8)
max_heap.insert(7)
max_heap.insert(6)
max_heap.insert(2)
max_heap.insert(5)
max_heap.insert(4)
print(max_heap.items)  # [None, 8, 7, 6, 2, 5, 4]
print(max_heap.delete())  # 8 을 반환해야 합니다!
print(max_heap.items)  # [None, 7, 5, 6, 2, 4]
print(max_heap.delete())
print(max_heap.items)