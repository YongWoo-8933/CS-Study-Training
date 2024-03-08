from __future__ import annotations
from typing import Any
import hashlib

class Node:

    def __init__(self, key: Any, value: Any, next: Node) -> None:
        self.key = key
        self.value = value
        self.next = next


class ChainedHash:

    def __init__(self, capacity: int) -> None:
        self.capacity = capacity
        self.table = [None] * capacity

    def get_hash_value(self, key: Any) -> int:
        if isinstance(key, int): return key % self.capacity
        return(int(hashlib.sha256(str(key).encode()).hexdigest(), 16) % self.capacity)
    
    def search(self, key: Any) -> Any:
        hash = self.get_hash_value(key)
        node = self.table[hash]
        
        while node is not None:
            if node.key == key: return node.value
            node = node.next

        return None
    
    def add(self, key: Any, value: Any) -> bool:
        hash = self.get_hash_value(key)
        node = self.table[hash]
        
        while node is not None:
            if node.key == key: return False
            node = node.next

        new_node = Node(key, value, self.table[hash])
        self.table[hash] = new_node
        return True
    
    def remove(self, key: Any) -> bool:
        hash = self.get_hash_value(key)
        node = self.table[hash]
        prev_node = None

        while node is not None:
            if node.key == key:
                if prev_node is None:
                    self.table[hash] = node.next
                else: 
                    prev_node.next = node.next
                return True
            prev_node = node
            node = node.next

        return False
    
    def dump(self) -> None:
        for i in range(self.capacity):
            node = self.table[i]
            print(i, end='')
            while node is not None:
                print(f"  -> {node.key} ({node.value})", end='')
                node = node.next
            print()


hash = ChainedHash(13)

while True:
    menu = input("수행할 작업을 선택해주세요\n(a: 추가, r: 제거, s: 검색, d: 덤프, q: 종료) => ")
    if menu == "a" or menu == "A":
        key = int(input("추가할 키를 적어주세요: "))
        value = input("추가할 값을 적어주세요: ")
        if hash.add(key, value): 
            print(f"{key}에 {value}가 추가되었습니다.") 
        else: 
            print("이미 존재하는 값입니다.")
    elif menu == "r" or menu == "R":
        key = int(input("삭제할 키를 적어주세요: "))
        if hash.remove(key): 
            print(f"{key}가 삭제되었습니다.") 
        else: 
            print("테이블에 존재하지 않는 값입니다.")
    elif menu == "s" or menu == "S":
        key = int(input("검색할 키를 적어주세요: "))
        result = hash.search(key)
        if result is not None: 
            print(f"{key}에 해당하는 값은 {result} 입니다.") 
        else: 
            print("해당 키의 값은 테이블에 존재하지 않습니다.")
    elif menu == "d" or menu == "D":
        hash.dump()
    elif menu == "q" or menu == "Q":
        break
    else: 
        continue