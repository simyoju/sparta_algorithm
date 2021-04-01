input = [3, 5, 6, 1, 2, 4]


def is_number_exist(number, array):
    # 이 부분을 채워보세요!
    ans = False
    for a in array:
        if a == number:
            ans = True

    return ans


result = is_number_exist(3, input)
print(result)