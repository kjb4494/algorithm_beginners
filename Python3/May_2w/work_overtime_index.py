"""
https://programmers.co.kr/learn/courses/30/lessons/12927?language=python3

야근 지수

문제 설명
    회사원 Demi는 가끔은 야근을 하는데요, 야근을 하면 야근 피로도가 쌓입니다.
    야근 피로도는 야근을 시작한 시점에서 남은 일의 작업량을 제곱하여 더한 값입니다.
    Demi는 N시간 동안 야근 피로도를 최소화하도록 일할 겁니다.
    Demi가 1시간 동안 작업량 1만큼을 처리할 수 있다고 할 때,
    퇴근까지 남은 N 시간과 각 일에 대한 작업량 works에 대해 야근 피로도를 최소화한 값을 리턴하는 함수 solution을 완성해주세요.

제한 사항
    works는 길이 1 이상, 20,000 이하인 배열입니다.
    works의 원소는 50000 이하인 자연수입니다.
    n은 1,000,000 이하인 자연수입니다.

입출력 예
    works 	    n 	result
    [4, 3, 3] 	4 	12
    [2, 1, 2] 	1 	6
    [1,1] 	    3 	0

입출력 예 설명
    입출력 예 #1
    n=4 일 때,
    남은 일의 작업량이 [4, 3, 3] 이라면 야근 지수를 최소화하기 위해 4시간동안 일을 한 결과는 [2, 2, 2]입니다.
    이 때 야근 지수는 2^2 + 2^2 + 2^2 = 12 입니다.

    입출력 예 #2
    n=1일 때,
    남은 일의 작업량이 [2,1,2]라면 야근 지수를 최소화하기 위해 1시간동안 일을 한 결과는 [1,1,2]입니다.
    야근지수는 1^2 + 1^2 + 2^2 = 6입니다.
"""


def test_case_solution(n, works):
    for i in range(n):
        works = sorted(works, reverse=True)
        if works[0] == 0:
            break
        works[0] -= 1
    result = 0
    for work in works:
        result += work ** 2
    print(works)
    return result


def solution(n, works):
    result = 0
    works.append(0)
    works.sort()
    for i in range(1, len(works)):
        tmp = works[-i] - works[-(i + 1)]
        if tmp * i < n:
            n -= tmp * i
            for j in range(1, i + 1):
                works[-j] -= tmp
        else:
            q = n // i
            n = n % i
            for j in range(1, i + 1):
                works[-j] -= q
            for j in range(1, n + 1):
                works[-j] -= 1
            break
    for i in works:
        result += i ** 2
    return result


def main_code():
    works = [1, 1, 35, 6, 8, 3, 2]
    n = 36
    print(test_case_solution(n, works))
    print("-" * 60)
    print(solution(n, works))


if __name__ == "__main__":
    main_code()
