input = "011110"


def find_count_to_turn_out_to_all_zero_or_all_one(string):
    # 이 부분을 채워보세요!
    cntZero = 0
    cntOne = 0

    if string[0] == '0':
        cntOne += 1
    elif string[0] == '1':
        cntZero += 1

    for i in range(len(string) - 1):
        if string[i] != string[i+1]:
            if string[i+1] == '0':
                cntOne += 1
            if string[i+1] == '1':
                cntZero += 1
    return min(cntOne, cntZero)


result = find_count_to_turn_out_to_all_zero_or_all_one(input)
print(result)