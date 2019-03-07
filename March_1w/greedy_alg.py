"""
https://programmers.co.kr/learn/courses/30/lessons/42883

큰 수 만들기

문제 설명
    어떤 숫자에서 k개의 수를 제거했을 때 얻을 수 있는 가장 큰 숫자를 구하려 합니다.
    예를 들어, 숫자 1924에서 수 두 개를 제거하면 [19, 12, 14, 92, 94, 24] 를 만들 수 있습니다. 이 중 가장 큰 숫자는 94 입니다.
    문자열 형식으로 숫자 number와 제거할 수의 개수 k가 solution 함수의 매개변수로 주어집니다. number에서 k 개의 수를 제거했을 때
    만들 수 있는 수 중 가장 큰 숫자를 문자열 형태로 return 하도록 solution 함수를 완성하세요.

제한 조건
    number는 1자리 이상, 1,000,000자리 이하인 숫자입니다.
    k는 1 이상 number의 자릿수 미만인 자연수입니다.

입출력 예
    number 	        k 	        return
    "1924" 	        2 	        "94"
    "1231234" 	    3 	        "3234"
    "4177252841" 	4 	        "775841"

"""

from decorators import time_measurement


def best_solution(number, k):
    stack = [number[0]]
    for num in number[1:]:
        while len(stack) > 0 and stack[-1] < num and k > 0:
            k -= 1
            stack.pop()
        stack.append(num)
    if k != 0:
        stack = stack[:-k]
    return ''.join(stack)


def solution(number, k):
    result = number
    start_index = 0
    num_length = len(result)
    for i in range(k):
        is_last_index = True
        for j in range(start_index, num_length - 1):
            if result[j] < result[j + 1]:
                is_last_index = False
                result = result[:j] + result[j + 1:]
                num_length -= 1
                start_index = j - 1 if j > 0 else 0
                break
        # 맨 마지막 숫자를 제거해야하는 상황일 때 대비
        if is_last_index:
            result = result[:-1]
            start_index = j - 1
    return result


@time_measurement
def main_code():
    for i in range(100000):
        solution("1231234", 4)
        # best_solution("1231234", 4)


if __name__ == "__main__":
    for i in range(10):
        main_code()
