input = [4, 6, 2, 9, 1]


def selection_sort(array):
    # 이 부분을 채워보세요!
    for i in range(len(array)-1):
        min = array[i]
        for j in range(len(array)-i-1):
            print(array[j])
            if array[i] < array[i+1]:
                continue
            else:
                pass
    return


selection_sort(input)
print(input) # [1, 2, 4, 6, 9] 가 되어야 합니다!