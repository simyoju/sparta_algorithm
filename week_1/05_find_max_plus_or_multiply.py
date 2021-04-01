input = [0, 3, 5, 6, 1, 2, 4]


def find_max_plus_or_multiply(array):
    # 이 부분을 채워보세요!
    sum = 0
    for number in array:
        if sum == 0 or number == 0 or number == 1:
            sum += number
        else:
            sum *= number
    return sum

result = find_max_plus_or_multiply(input)
print(result)