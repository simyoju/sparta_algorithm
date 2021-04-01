input = [4, 6, 2, 9, 1]


def bubble_sort(array):
    # 이 부분을 채워보세요!
    # a = b, b = a 이용
    # 두번째 원소부터 돌아라
    cnt = len(array)-1
    print(cnt)
    while cnt is not 0:
        for i in range(len(array)):
            if i == 0:
                print("I am index[0]")
                continue
            # fir = array[i-1], sec = array[i]
            if array[i - 1] > array[i]:
                cnt -= 1
                print(cnt)
                print(array[i - 1], array[i])
                array[i - 1], array[i] = array[i], array[i - 1]
                print(array)
            # cnt = len(array) - 1
    return array


bubble_sort(input)
print(input)  # [1, 2, 4, 6, 9] 가 되어야 합니다!