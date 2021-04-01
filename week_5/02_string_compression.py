input = "abcabcabcabcdededededede"


def string_compression(string):
    # 입력받은 문자열을 길이의 절반까지 다 잘라서 저장
    len_str = len(string)
    ans_arr = []
    ans_arr_len = []

    for split_size in range(1, len_str // 2 + 1) :
        ans = ""
        split_arr = [
            string[i : i+split_size] for i in range(0, len_str, split_size)
        ]
        # 반복되는 여부 파악
        # 앞에꺼 뒤에꺼 비교. prev, cur
        cnt = 1

        for j in range(1, len(split_arr)):
            prev, cur = split_arr[j-1], split_arr[j]
            # print(prev, cur)
            if prev == cur:
                cnt += 1
            else:
                # 둘이 다르면 넘어가야지.. 그걸 어케하지..
                # !달라지면 추가해야지
                if cnt > 1:
                    ans += (str(cnt) + prev)
                else:
                    ans += prev
                cnt = 1

        # !! 꼬다리 처리
        if cnt > 1:
            ans += (str(cnt) + split_arr[-1])
        else:
            ans += split_arr[-1]
        ans_arr.append(ans)
        ans_arr_len.append(len(ans))

    return min(ans_arr_len)


print(string_compression(input))  # 14 가 출력되어야 합니다!