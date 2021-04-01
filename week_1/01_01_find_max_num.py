input = [3, 5, 6, 1, 2, 4]


def find_max_num(array):
    # 이 부분을 채워보세요!
    res = array[0]
    for num in array:
        if res <= num:
            res = num
    return res


result = find_max_num(input)
print(result)