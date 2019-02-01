"""
1.7 행렬회전 : 이미지를 표현하는 N * N 행렬이 있다.
이미지의 각 픽셀은 4바이트로 표현된다.
이때, 이미지를 90도 회전시키는 메서드를 작성하라.
행렬을 추가로 사용하지 않고서도 할 수 있겠는가?
"""

from decorators import time_measurement
from random import randint


# 픽셀이 4바이트라니까 int형 데이터로 체움.
"""
알고리즘
1 2 3
4 5 6
7 8 9
--> 90도 회전하면 7 4 1 8 5 2 9 6 3이 된다.
행렬의 행(또는 열)의 크기를 N이라고 가정하면,
행렬을 일차원 리스트로 풀었을 때(1 2 3 4 5 6 7 8 9) 뒤에서 부터 각각 N씩 건너뛴 값들이 순서대로 나열됨.

문제 해결 방식
1. 리스트를 일차원으로 풀고 뒤집는다. 9 8 7 6 5 4 3 2 1
2. N번째 데이터부터 N씩 건너뛴 값들을 나열한다. --> 7 4 1
3. N-1번째 데이터부터 N씩 건너뛴 값들을 나열한다. --> 8 5 2
4. N-2번째 데이터부터 N씩 건너뛴 값들을 나열한다. --> 9 6 3
5. 2~4번 과정을 묶는다.
6. 결과물을 기존 행렬에 치환시킨다.
"""


@time_measurement
def solution(image_matrix):
    data_list = [data for row in image_matrix for data in row][::-1]        # Constant n^2
    N = len(image_matrix)                                                   # Constant 1
    rows = 0                                                                # Constant 1
    cols = 0                                                                # Constant 1
    for i in range(N, 0, -1):
        for j in range(i, N * N + 1, N):
            image_matrix[rows][cols] = data_list[j - 1]                     # Constant n^2
            cols += 1                                                       # Constant n^2
        rows += 1                                                           # Constant n
        cols = 0                                                            # Constant n

    # T(n) = 3 + 2n + 3n^2
    # O(n^2)


def main_code():
    N = randint(1, 9)
    image_matrix = [[randint(0, 9) for j in range(N)] for i in range(N)]
    for row in image_matrix:
        for data in row:
            print(data, end=" ")
        print()
    solution(image_matrix)
    for row in image_matrix:
        for data in row:
            print(data, end=" ")
        print()


if __name__ == "__main__":
    for i in range(10):
        main_code()
        print()
