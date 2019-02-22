#### 구현
  * 사용되는 객체
    - binary_tree
      - 이진 탐색 트리 객체 재활용(February_3w.binary_search_tree)
      - 데이터가 무작위로 배치되는 이진 트리(binary_tree) 객체로 수정
      
    - linked_list
      - 연결리스트 객체 재활용(January_5w.linked_list)
      
    - binary_search_tree
      - binary_tree를 부모 객체로 수정

  * 깊이의 리스트 - list_of_depth
    - 이진 트리의 전위 순회 알고리즘을 이용해 깊이에 따른 데이터값을 가진 이차배열을 생성함
    - 생성한 이차배열을 이용해 연결리스트 객체들을 생성함
  
  * 균형 확인 - check_balance
    - 전위 순회 알고리즘에서 깊이가 1인 노드부터 왼쪽과 오른쪽으로 갈리는 특성을 이용함
    - 루트 노드의 왼쪽 노드가 Null이면 왼쪽 트리의 깊이는 0임
  
  * BST 검증 - BST_verification
