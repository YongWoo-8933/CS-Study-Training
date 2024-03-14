from typing import Any


class FixedQueue:

    class Empty(Exception): pass

    class Full(Exception): pass

    def __init__(self, capacity: int = 256) -> None:
        self.queue = [None] * capacity
        self.capacity = capacity
        self.num = 0
        self.front = 0
        self.rear = 0

    def __len__(self) -> int:
        return self.num
    
    def is_empty(self) -> bool:
        return self.num <= 0
    
    def is_full(self) -> bool:
        return self.num >= self.capacity
    
    def enqueue(self, value: Any) -> None:
        if self.is_full(): raise FixedQueue.Full
        self.queue[self.rear] = value
        self.rear += 1
        self.num += 1
        if self.rear == self.capacity: self.rear = 0
    
    def dequeue(self) -> Any:
        if self.is_empty(): raise FixedQueue.Empty
        temp = self.queue[self.front]
        self.front += 1
        self.num -= 1
        if self.front == self.capacity: self.front = 0
        return temp
    
    def peek(self) -> Any:
        if self.is_empty(): raise FixedQueue.Empty
        return self.queue[self.front]
    
    def clear(self) -> None:
        self.front = self.rear = self.num = 0

    def find(self, value: Any) -> Any:
        for i in range(self.num):
            index = (i + self.front) % self.capacity
            if self.queue[index] == value: return index 
        return -1
    
    def count(self, value: Any) -> int:
        s = 0
        for i in range(self.num):
            index = (i + self.front) % self.capacity
            if self.queue[index] == value: s += 1
        return s
    
    def __contains__(self, value: Any) -> bool:
        return self.count(value) > 0
    
    def dump(self) -> None:
        if self.is_empty(): 
            print("큐가 비어있어요.")
        else:
            print(*[self.queue[(i + self.front) % self.capacity] for i in range(self.num)])


fixed_queue = FixedQueue(capacity=16)


while True:
    menu = input("수행할 작업을 선택해주세요\n(eq: 인큐, dq: 디큐, pk: 피크, cl: 클리어, s: 검색, co: 카운트, d: 덤프, q: 종료) => ")
    if menu == "eq" or menu == "EQ":
        value = input("추가할 값을 적어주세요: ")
        fixed_queue.enqueue(value)
        print(f"큐에 {value}를 인큐했어요") 
    elif menu == "dq" or menu == "DQ":
        try:
            value = fixed_queue.dequeue()
            print(f"큐에서 {value}를 디큐했어요") 
        except FixedQueue.Empty:
            print("큐가 비어있어 디큐할 수 없어요")
    elif menu == "pk" or menu == "PK":
        try:
            value = fixed_queue.peek()
            print(f"큐 프론트 값: {value}") 
        except FixedQueue.Empty:
            print("큐가 비어있어 픽할 수 없어요")
    elif menu == "cl" or menu == "CL":
        value = fixed_queue.clear()
        print("큐 클리어 완료")
    elif menu == "s" or menu == "S":
        value = input("검색할 값을 적어주세요: ")
        index = fixed_queue.find(value)
        if index < 0: 
            print(f"{value}는 큐에 존재하지 않는 값이에요") 
        else: 
            print(f"{value}는 큐의 {index} 인덱스에 있어요")
    elif menu == "co" or menu == "CO":
        value = input("카운트할 값을 적어주세요: ")
        print(f"{value}는 큐에 {fixed_queue.count(value)}개 있어요") 
    elif menu == "d" or menu == "D":
        fixed_queue.dump()
    elif menu == "q" or menu == "Q":
        break
    else: 
        continue
    