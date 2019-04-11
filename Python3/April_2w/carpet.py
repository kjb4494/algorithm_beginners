# https://programmers.co.kr/learn/courses/30/lessons/42842?language=java

# 그림 있어서 문제 쓰기 귀찮음


def solution(brown, red):
    # 전체 넓이를 구함
    rect = brown + red
    # a는 넓이의 루트값보다 작음 (어짜피 값을 구하면 브레이크 되므로 굳이 할 필요는 없음)
    for a in range(1, int(rect ** 0.5) + 1):
        # 넓이를 a로 나눈 값이 나눠떨어지면 답의 후보가 됨 (rect % a == 0)으로 해도됨 / 그냥 이게 더 간지나 보여서 쓴 거)
        if (rect / a).is_integer():
            b = rect // a
            # 후보 중 빨간색 면적까지 조건을 맞추면 답임
            if (a - 2) * (b - 2) == red:
                answer = [b, a]
                break
    return answer


# 수학으로 풀이
# x^2 + ax + b = 0 이차방정식의 해
def best_solution(brown, red):
    a = (brown + 4) // 2
    b = brown + red
    c = (a * a - 4 * b) ** 0.5
    return [(a + c) // 2, (a - c) // 2]


def main_code():
    print(solution(24, 24))
    print(best_solution(24, 24))


if __name__ == "__main__":
    main_code()
