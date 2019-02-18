"""
4.1 노드사이의 경로: 방향 그래프가 주어졌을 때
두 노드 사이에 경로가 존재하는지 확인하는 알고리즘을 작성하라.
힌트 #127
"""

from random import randint
from decorators import time_measurement

#                 0  1  2  3  4  5  6  7  8
example_graph = [[0, 0, 1, 0, 0, 1, 0, 0, 0],  # 0
                 [0, 0, 0, 0, 0, 0, 1, 0, 0],  # 1
                 [0, 0, 0, 0, 0, 0, 1, 0, 0],  # 2
                 [0, 0, 0, 0, 1, 0, 0, 0, 0],  # 3
                 [0, 0, 0, 0, 0, 1, 0, 0, 0],  # 4
                 [0, 0, 0, 1, 0, 0, 0, 1, 0],  # 5
                 [0, 0, 0, 0, 0, 0, 0, 0, 0],  # 6
                 [0, 0, 1, 0, 0, 0, 0, 0, 1],  # 7
                 [0, 0, 0, 0, 0, 0, 0, 0, 0]]  # 8


@time_measurement
def solution(graph, src, dst):
    # 경로를 추적할 노드의 대기 배열
    nodes_to_visit = [src]
    # 경로 추적을 마친 노드 배열
    visited_node = []
    while nodes_to_visit:
        # 경로 추적이 끝난 노드일 경우 대기 배열에서 삭제하고 다음으로 넘어감
        # 같은 작업으로 인한 연산 처리량을 줄이고 무한루프를 방지
        if nodes_to_visit[0] in visited_node:
            del nodes_to_visit[0]
            continue
        # 다음 노드 경로를 추적하고 목적지 노드에 도달하면 True를 반환함
        for i in range(len(graph[nodes_to_visit[0]])):
            if graph[nodes_to_visit[0]][i] >= 1:
                if i == dst:
                    return True
                else:
                    # 목적지 노드가 아닐 경우 대기 배열에 추가
                    nodes_to_visit.append(i)
        # 추적이 끝난 노드로 배열에 추가하고 대기 배열에서 삭제
        visited_node.append(nodes_to_visit[0])
        del nodes_to_visit[0]
    return False


def main_code():
    i, j = randint(0, 8), randint(0, 8)
    if solution(example_graph, i, j):
        print("{}에서 {}로 가는 경로는 존재한다.".format(i, j))
    else:
        print("{}에서 {}로 가는 경로는 존재하지 않는다.".format(i, j))


if __name__ == "__main__":
    for i in range(20):
        main_code()
        print()
