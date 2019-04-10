"""
https://programmers.co.kr/learn/courses/30/lessons/43238?language=python3

입국심사

문제 설명
    n명이 입국심사를 위해 줄을 서서 기다리고 있습니다. 각 입국심사대에 있는 심사관마다 심사하는데 걸리는 시간은 다릅니다.
    처음에 모든 심사대는 비어있습니다. 한 심사대에서는 동시에 한 명만 심사를 할 수 있습니다.
    가장 앞에 서 있는 사람은 비어 있는 심사대로 가서 심사를 받을 수 있습니다.
    하지만 더 빨리 끝나는 심사대가 있으면 기다렸다가 그곳으로 가서 심사를 받을 수도 있습니다.

    모든 사람이 심사를 받는데 걸리는 시간을 최소로 하고 싶습니다.

    입국심사를 기다리는 사람 수 n, 각 심사관이 한 명을 심사하는데 걸리는 시간이 담긴 배열 times가 매개변수로 주어질 때,
    모든 사람이 심사를 받는데 걸리는 시간의 최솟값을 return 하도록 solution 함수를 작성해주세요.


제한사항
    입국심사를 기다리는 사람은 1명 이상 1,000,000,000명 이하입니다.
    각 심사관이 한 명을 심사하는데 걸리는 시간은 1분 이상 1,000,000,000분 이하입니다.
    심사관은 1명 이상 100,000명 이하입니다.

입출력 예
    n 	times 	return
    6 	[7, 10] 	28

입출력 예 설명
    가장 첫 두 사람은 바로 심사를 받으러 갑니다.
    7분이 되었을 때, 첫 번째 심사대가 비고 3번째 사람이 심사를 받습니다.
    10분이 되었을 때, 두 번째 심사대가 비고 4번째 사람이 심사를 받습니다.
    14분이 되었을 때, 첫 번째 심사대가 비고 5번째 사람이 심사를 받습니다.
    20분이 되었을 때, 두 번째 심사대가 비지만 6번째 사람이 그곳에서 심사를 받지 않고
    1분을 더 기다린 후에 첫 번째 심사대에서 심사를 받으면 28분에 모든 사람의 심사가 끝납니다.

"""

# 베스트코드 없음


# 할당된 시간 내에 입국 심사를 끝낼 수 있는지의 여부를 반환한다.
# 끝낼 수 있으면 True, 끝낼 수 없으면 False
def is_feasibility(value, n, times):
    count = n
    index = 0
    while count > 0 and index < len(times):
        count -= value // times[index]
        index += 1
    return not count > 0


def solution(n, times):
    minimum = 1
    maximum = max(times) * n
    # 아래 과정을 이분탐색으로 수행한다. (최소값과 최대값이 수렴할 때까지)
    while minimum + 1 < maximum:
        # mid 값은 각 심사관이 소모할 수 있는 최대 시간이다.
        mid = (minimum + maximum) / 2
        # 만약 심사가 가능한 값이라면 최대값을 줄이고 불가능한 값이라면 최소값을 늘린다.
        if is_feasibility(mid, n, times):
            maximum = mid
        else:
            minimum = mid + 1
    # 이분탐색을 끝내고 최소값과 최대값 중에 어떤 정수값을 사용할지 결정한다.
    return int(minimum) if is_feasibility(int(minimum), n, times) else int(maximum)


def main_code():
    print(solution(6, [7, 10]))


if __name__ == "__main__":
    main_code()
