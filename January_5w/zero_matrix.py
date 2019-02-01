"""
1.8  0행렬 : M * N 행렬의 한 원소가 0일 경우,
해당 원소가 속한 행과 열의 모든 원소를 0으로 설정하는 알고리즘을 작성하라.
"""

from decorators import time_measurement
from random import randint


@time_measurement
def solution(matrix):
    rows = len(matrix)                          # Constant 2
    cols = len(matrix[0])                       # Constant 2
    zero_list = []                              # Constant 1
    # 행렬이 없을 경우 함수 종료
    if rows <= 0 or cols <= 0:                  # Constant 2
        return
    # 0의 위치를 탐색한다.
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 0:               # Constant n^2
                zero_list.append((i, j))        # Constant n^2
    # 탐색된 좌표의 행과 열의 값을 전부 0으로 만든다.
    for i, j in zero_list:
        for k in range(rows):
            matrix[k][j] = 0                    # Constant n^2
        for l in range(cols):
            matrix[i][l] = 0                    # Constant n^2

    # T(n) = 7 + 4n^2
    # O(n^2)


def main_code():
    M = randint(2, 20)
    N = randint(2, 20)
    random_matrix = [[randint(0, 9) for j in range(M)] for i in range(N)]
    for row in random_matrix:
        for data in row:
            print(data, end=" ")
        print()
    solution(random_matrix)
    for row in random_matrix:
        for data in row:
            print(data, end=" ")
        print()


if __name__ == "__main__":
    for i in range(10):
        main_code()
        print()
