input = 21


def find_prime_list_under_number(number):
    # 이 부분을 채워보세요!
    res = []

    for num in range(1, number):
        countZero = 0

        for n in range(1, num):
            if num % n == 0:
                countZero += 1

        if countZero == 1:
            res.append(num)

    return res

result = find_prime_list_under_number(input)
print(result)