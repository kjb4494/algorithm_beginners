#### 구현
  * 한 개로 세 개 - three_in_one
    - 주어진 배열을 3등분하여 3개의 스택으로 만듦
    - 마지막 스택은 배열의 3등분 하고 남은 나머지 공간도 가져감
    - 각각의 스택은 주어진 공간밖에 사용하지 못 함
    - 유동성 없음
  * 유연한 한 개로 세 개 - flexible_three_in_one
    - 3개의 스택을 생성하고 관리하는 객체로 구성됨
    - 크기가 정해진 빈 배열을 받아 3개의 스택이 공간을 유동적으로 사용할 수 있음
    - 3개의 스택은 독립적이지만 최대로 사용할 수 있는 공간은 배열의 크기만큼으로 공유함
  * 스택Min - stack_min
    - O(1) 시간복잡도로 최솟값을 구하기 위해 메모리를 배로 사용함
    - 최근 최솟값과 최솟값의 순서를 기억하는 배열을 pop, push가 일어날 때마다 갱신함