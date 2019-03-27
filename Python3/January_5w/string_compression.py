"""
1.6 문자열 압축 : 반복되는 문자의 개수를 세는 방식의 기본적인 문자열 압축 메서드를 작성하라. 예를 들어 문자열 aabcccccaaa를 압축하면 a2b1c5a3이 된다.
만약 ‘압축된’ 문자열의 길이가 기존 문자열의 길이보다 길다면 기존 문자열을 반환해야 한다. 문자열은 대소문자 알파벳(a~z)으로만 이루어져 있다.
"""
from random import randint, choice
from decorators import time_measurement


@time_measurement
def solution(original_string):
    # 문자열 길이가 2보다 작으면 원문 반환
    if len(original_string) < 2:                    # Constant 1
        return original_string
    result_string = priv_ch = original_string[0]    # Constant 2
    count = 1                                       # Constant 1
    for ch in original_string[1:]:                  # Constant n
        if priv_ch != ch:                           # Constant n
            result_string += str(count) + ch        # Constant 2n
            count = 1                               # Constant n
        else:
            count += 1
        priv_ch = ch                                # Constant n
    if count:                                       # Constant 1
        result_string += str(count)                 # Constant 2
    return result_string if len(result_string) <= len(original_string) else original_string     # Constant 3

    # T(n) = 10 + 6n
    # O(n)


def main_code():
    length = randint(0, 40)
    string_pool = ['a', 'b']
    test_string = ""
    for i in range(length):
        test_string += choice(string_pool)
    print("원문: {}".format(test_string))
    print("압축: {}".format(solution(test_string)))


if __name__ == "__main__":
    for i in range(20):
        main_code()
        print()
