from typing import Any


class FixedStack:

    class Empty(Exception): pass

    class Full(Exception): pass

    def __init__(self, capacity: int = 256) -> None:
        self.stack = [None] * capacity
        self.capacity = capacity
        self.pointer = 0

    def __len__(self) -> int:
        return self.pointer
    
    def is_empty(self) -> bool:
        return self.pointer <= 0
    
    def is_full(self) -> bool:
        return self.pointer >= self.capacity
    
    def push(self, value: Any) -> None:
        if self.is_full(): raise FixedStack.Full
        self.stack[self.pointer] = value
        self.pointer += 1
        return self.pointer >= self.capacity
    
    def pop(self) -> Any:
        if self.is_empty(): raise FixedStack.Empty
        self.pointer -= 1
        return self.stack[self.pointer]
    
    def peek(self) -> Any:
        if self.is_empty(): raise FixedStack.Empty
        return self.stack[self.pointer - 1]
    
    def clear(self) -> None:
        self.pointer = 0

    def find(self, value: Any) -> Any:
        for i in range(self.pointer - 1, -1, -1):
            if self.stack[i] == value: return i 
        return -1
    
    def count(self, value: Any) -> int:
        s = 0
        for i in self.stack:
            if i == value: s += 1
        return s
    
    def __contains__(self, value: Any) -> bool:
        return self.count(value) > 0
    
    def dump(self) -> None:
        if self.is_empty(): 
            print("스택이 비어있어요.")
        else:
            print(self.stack[:self.pointer])


fixed_stack = FixedStack(capacity=16)


while True:
    menu = input("수행할 작업을 선택해주세요\n(pu: 푸시, po: 팝, pk: 피크, cl: 클리어, s: 검색, co: 카운트, d: 덤프, q: 종료) => ")
    if menu == "pu" or menu == "PU":
        value = input("추가할 값을 적어주세요: ")
        fixed_stack.push(value)
        print(f"스택에 {value}가 추가됐어요") 
    elif menu == "po" or menu == "PO":
        try:
            value = fixed_stack.pop()
            print(f"스택에서 {value}를 팝했어요") 
        except FixedStack.Empty:
            print("스택이 비어있어 팝할 수 없어요")
    elif menu == "pk" or menu == "PK":
        try:
            value = fixed_stack.peek()
            print(f"스택 최상단 값: {value}") 
        except FixedStack.Empty:
            print("스택이 비어있어 픽할 수 없어요")
    elif menu == "cl" or menu == "CL":
        value = fixed_stack.clear()
        print("스택 클리어 완료")
    elif menu == "s" or menu == "S":
        value = input("검색할 값을 적어주세요: ")
        index = fixed_stack.find(value)
        if index < 0: 
            print(f"{value}는 스택에 존재하지 않는 값이에요") 
        else: 
            print(f"{value}는 스택의 {index + 1}번째 값에 있어요")
    elif menu == "co" or menu == "CO":
        value = input("카운트할 값을 적어주세요: ")
        print(f"{value}는 스택에 {fixed_stack.count(value)}개 있어요") 
    elif menu == "d" or menu == "D":
        fixed_stack.dump()
    elif menu == "q" or menu == "Q":
        break
    else: 
        continue
    