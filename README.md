# Python_Data-Structure

## 실습환경
- https://www.fun-coding.org/
- Language : Python 3.6
- Tool : Visual-Studio-Code

## 대표적인 자료구조
- 배열
- 큐 : FIFO(선입선출)
- 스택 : LIFO(후입선출)
- 힙
- 트리
- 링크드 리스트
- 해쉬 테이블

## Queue
- Enqueue: queue에 데이터를 넣는 기능
- Dequeue: queue에 데이터를 꺼내는 기능
- Python에서는 Queue(), LifoQueue(), PriorityQueue()를 제공
    + Queue(): 가장 일반적인 큐
    + LifoQueue(): 나중에 입력된 데이터가 먼저 출력(스택구조)
    + PriorityQueue(): 데이터마다 우선순위를 넣어서, 우선순위가 높은 순으로 데이터 출력

## Linked List
- 연결 리스트
- 배열은 순차적으로 연결된 공간에 데이터를 나열하는 데이터 구조라면 링크드 리스트는 떨어진 곳에 존재하는 데이터를 화살표로 연결해서 관리하는 데이터 구조
    - 기본 구조 / 용어
        + 노드: 데이터 저장 단위(데이터값, 포인터)로 구성
        + 포인터: 각 노드 안에서, 다음이나 이전의 노드와의 연결 정보를 가지고 있는 공간
    - 장점
        + 미리 데이터 공간을 할당하지 않아도 됨(배열은 미리 할당 필요)
    - 단점
        + 연결을 위한 별도 데이터 공간이 필요하므로, 저장공간 효율이 높지 않음
        + 연결 정보를 찾는 시간이 필요하므로 접근 속도가 느림
        + 중간 데이터 삭제시, 앞뒤 데이터의 연결을 재구성해야 하는 부가적인 작업필요

- 이중 연결 리스트
    - 장점:
        + 양방향으로 연결되어 있어서 노드 탐색이 양쪽으로 모두 가능

## 해쉬 테이블
- 해쉬 구조
    - Hash table: 키(Key)에 데이터(Value)를 저장하는 데이터 구조
        + Key를 통해 바로 데이터를 받아올 수 있으므로, 속도가 빠름
        + Python Dictionary
        + 보통 배열로 미리 Hash Table 사이즈만큼 생성 후에 사용(공간과 탐색시간을 맞바꾸는 기법)
        + Python에서는 해쉬를 별도 구현할 이유가 없다. (딕셔너리 타입을 사용)
- 용어
    + 해쉬(Hash): 임의 값을 고정 길이로 변환하는 것
    + 해쉬 테이블(Hash Table): 키 값의 연산에 의해 직접 접근이 가능한 데이터 구조
    + 해싱 함수(Hashing Function): Key에 대해 산술 연산을 이용해 데이터 위치를 찾을 수 있는 함수
    + 해쉬 값(Hash Value) 또는 해쉬 주소(Hash Address): Key를 해싱 함수로 연산해서, 해쉬 값을 알아내고, 이를 기반으로 해쉬 테이블에서 해당 Key에 대한 데이터 위치를 일관성있게 찾을 수 있음
    + 슬롯(Slot): 한 개의 데이터를 저장할 수 있는 공간
    + 저장할 데이터에 대해 Key를 추출할 수 있는 별도 함수도 존재할 수 있음

- 장점
    + 데이터 저장/읽기 속도가 빠름(검색 속도가 빠르다.)
    + 해쉬는 키에 대한 데이터가 있는지(중복) 확인이 쉬움.
- 단점
    + 일반적으로 저장공간이 좀더 많이 필요
    + 여러 키에 해당하는 주소가 동일한 경우 충돌을 해결하기 위한 별도 자료구조가 필요
- 주요 용도
    + 검색이 많이 필요한 경우
    + 저장, 삭제 읽기가 빈번한 경우
    + 캐쉬 구현시(중복 확인이 쉽기 떄문에)

- 충돌(Collision) 해결 알고리즘
    - Chaining 기법: 개방 해싱 또는 Open Hashing 기법 중 하나
        + 해쉬 테이블 저장공간 외의 공간을 활용하는 기법
        + 충돌이 일어나면, 링크드 리스트라는 자료구조를 사용해서, 링크드 리스트로 데이터를 추가로 뒤에 연결시켜서 저장하는 기법
    - Linear Probing 기법: 패쇄 해싱 또는 Close Hashing 기법 중 하나
        + 해쉬 테이블 저장공간 안에서 충돌 문제를 해결하는 기법
        + 충돌이 일어나면, 해당 hash address의 다음 address부터 맨 처음 나오는 빈공간에 저장하는 기법
        + 저장공간 활용도를 높이기 위한 기법

- SHA(Secure Hash Algorithm) 해쉬 알고리즘
    + 어떤 데이터도 유일한 고정된 크기의 고정값을 리턴해주므로, 해쉬 함수로 유용하게 활용 가능

- 시간복잡도 
    + 일반적인 경우(충돌이 없는 경우) O(1)
    + 최악의 경우(충돌이 모두 발생한 경우 O(n)
    + 검색에서 해쉬 테이블의 사용 예
        + 16개의 배열에 데이터를 저장하고, 검색할 때 O(n)
        + 16개의 데이터 저장공간을 가진 위의 해쉬 테이블에 데이터를 저장하고, 검색할 때 O(1)

## Heap
- 힙(heap): 데이터에서 최대값과 최소값을 빠르게 찾기 위해 고안된 완전 이진 트리
    - 완전이진트리: 노드를 삽입할 때 최하단 왼쪽 노드부터 차례대로 삽입하는 트리
- 힙 사용 이유
    + 배열에 데이터를 넣고, 최대,최소값을 찾으려면 O(n)이 걸림
    + 힙에 데이터를 넣고, 최대,최소값을 찾으면 O(logn)이 걸려서 더 빠름
    + 우선순위 큐와 같이 최대값 또는 최소값을 빠르게 찾아야 하는 자료구조 및 알고리즘 구현 등에 활용됨

- 힙 구조
    + 힙은 최대값을 구하기 위한 구조 (최대 힙, Max Heap)와, 최소값을 구하기 위한 구조(최소 힙, Min heap)로 분류
    - 다음 두 가지 조건을 가지는 자료구조
        1. 각 노드의 값은 해당 노드의 자식 노드가 가진 값보다 크거나 같다.(최대힙의 경우)
            + 최소 힙의 경우는 각 노드의 값은 해당 노드의 자식 노드가 가진 값보다 크거나 작음
        2. 완전 이진 트리 형태를 가짐

- 힙과 이진 탐색 트리의 공통점/차이점
    - 공통점
        + 모두 이진 트리임
    - 차이점
        + 힙은 각 노드의 값이 자식 노드보다 크거나 같은(Max Heap의 경우)
        + 이진 탐색 트리는 왼쪽 자식 노드의 값이 가장 작고, 그 다음 부모 노드, 그 다음 오른쪽 자식 노드 값이 가장 큼
        + 힙은 이진 탐색 트리의 조건인 자식 노드에서 작은 값은 왼쪽, 큰 값은 오른쪽이라는 조건이 없음
        + 힙의 왼쪽 및 오른쪽 자식 노드의 값은 오른쪽이 클 수도 있고, 왼쪽이 클 수도 있음
    
    - 이진 탐색 트리는 탐색을 위한 구조
    - 힙은 최대/최소값 검색을 위한 구조

- 시간 복잡도
    - n개의 노드를 가지는 heap에 데이터 삽입 또는 삭제시, 최악의 경우 root노드에서 leaf노드까지 비교해야 하므로 h(tree depth) = log2n에 가까우므로, 시간 복작도는 O(logn)

## 정렬 알고리즘
- 참고: https://ieatt.tistory.com/11?category=615643
  
- 버블정렬(bubble sort): 인접합 두 데이터를 비교해서, 앞에 있는 데이터가 뒤에 있는 데이터보다 크면, 자리를 바꾸는 알고리즘
  - 시간 복잡도 - O(n2)-반복문이 두개
    - 완전 정렬된 상태라면 최선은 O(n)

- 삽입정렬(insertion sort): 2번째 인덱스부터 시작하여 그 앞쪽(왼쪽)의 원소들과 비교하여 삽입할 위치를 지정한 후, 뒤로 옮기고 지정된 자리에 자료를 삽입하여 정렬하는 알고리즘
  - 현재 선택된 데이터 이전의 데이터들은 항상 정렬된 상태이다.
  - 시간 복잡도
    - 최선 O(n)
    - 최악 O(n2)