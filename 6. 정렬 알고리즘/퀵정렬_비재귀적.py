"""
=> 퀵 정렬의 비재귀적 구현 방식으로, 간단한 Stack을 통해 구현
"""
from typing import Any


class FixedStack:

    class Empty(Exception): pass

    class Full(Exception): pass

    def __init__(self, capacity: int = 256) -> None:
        self.stack = [None] * capacity
        self.capacity = capacity
        self.pointer = 0
    
    def is_empty(self) -> bool:
        return self.pointer <= 0
    
    def push(self, value: Any) -> None:
        if self.pointer >= self.capacity: raise FixedStack.Full
        self.stack[self.pointer] = value
        self.pointer += 1
        return self.pointer >= self.capacity
    
    def pop(self) -> Any:
        if self.is_empty(): raise FixedStack.Empty
        self.pointer -= 1
        return self.stack[self.pointer]


def quick_sorted(lst: list) -> list:
    n = len(lst)
    stack = FixedStack(n)
    stack.push((0, n-1))

    while not stack.is_empty():
        pointer_left, pointer_right = left, right = stack.pop()
        pivot = lst[(left + right)//2]

        print(f"list[{left}] ~ list[{right}]:", *lst[left: right + 1])

        while pointer_left <= pointer_right:
            while lst[pointer_left] < pivot: pointer_left += 1
            while lst[pointer_right] > pivot: pointer_right -= 1
            if pointer_left <= pointer_right:
                lst[pointer_left], lst[pointer_right] = lst[pointer_right], lst[pointer_left] 
                pointer_left += 1
                pointer_right -= 1
    
        if left < pointer_right: stack.push((left, pointer_right))
        if right > pointer_left: stack.push((pointer_left, right))
    return lst


lst_1 = [1, 3, 9, 94, 82, 4, 11, 77, 7, 88, 8, 104, 6]

print(quick_sorted(lst_1))