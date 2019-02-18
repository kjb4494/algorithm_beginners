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
    nodes_to_visit = [src]
    visited_node = []
    while nodes_to_visit:
        if nodes_to_visit[0] in visited_node:
            del nodes_to_visit[0]
            continue
        for i in range(len(graph[nodes_to_visit[0]])):
            if graph[nodes_to_visit[0]][i] >= 1:
                if i == dst:
                    return True
                else:
                    nodes_to_visit.append(i)
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
