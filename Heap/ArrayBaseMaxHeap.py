# ArrayBaseMaxHeap.py

# 배열 기반 최대 히프 클래스
class ArrayBaseMaxHeap :

    # 배열 기반 최대 히프 초기화 함수
    def __init__(self, len) :
        self.data = [0 for _ in range(len)]
        self.count = 0
        self.max_len = len

    # 배열 기반 최대 히프 공백 검사 함수
    def is_empty(self) :
        return self.count == 0

    # 배열 기반 최대 히프 포화 검사 함수
    def is_full(self) :
        return self.count == (self.max_len - 1)

    # 배열 기반 최대 히프 삽입 함수
    def insert_max_heap(self, data) :
        self.count += 1
        i = self.count

        while i != 1 and data > self.data[i // 2] :
            self.data[i] = self.data[i // 2]
            i //= 2

        self.data[i] = data

    # 배열 기반 치대 히프 삭제 함수
    def delete_max_heap(self) :
        pass

    def inorder_traversal(self, idx) :
        if idx > self.count :
            return

        inorder_traversal(2 * idx);


if __name__ == '__main__' :

    # 배열 기반 최대 히프 객채 선언
    Heap = ArrayBaseMaxHeap(50)

    # 배열 기반 최대 히프 공백 확인
    print("Heap.is_empty() : "+ str(Heap.is_empty()))
    '''
    Heap.is_empty() : True
    '''

    # 배열 기반 최대 히프 포화 확인
    print("Heap.isfull() : " + str(Heap.is_full()))
    '''
    Heap.isfull() : False
    '''

    # 배열 기반 최대 히프 데이터 삽입
    Heap.insert_max_heap(10)
    Heap.insert_max_heap(30)
    Heap.insert_max_heap(20)
    Heap.insert_max_heap(60)
    Heap.insert_max_heap(50)
    Heap.insert_max_heap(40)
    '''
                60
        50              40
    10      30      20
    '''
