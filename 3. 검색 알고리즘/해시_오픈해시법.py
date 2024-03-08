from __future__ import annotations
from typing import Any
import hashlib
from enum import Enum


class Status(Enum):
    OCCUPIED = 0
    EMPTY = 1
    DELETED = 2


class Bucket:

    def __init__(self, key: Any = None, value: Any = None, status: Status = Status.EMPTY) -> None:
        self.key = key
        self.value = value
        self.status = status
    
    def set(self, key: Any, value: Any, status: Status) -> None:
        self.key = key
        self.value = value
        self.status = status
    
    def set_status(self, status: Status) -> None:
        self.status = status
    

class OpenHash:

    def __init__(self, capacity: int) -> None:
        self.capacity = capacity
        self.table = [Bucket()] * capacity

    def get_hash_value(self, key: Any) -> int:
        if isinstance(key, int): return key % self.capacity
        return(int(hashlib.sha256(str(key).encode()).hexdigest(), 16) % self.capacity)
    
    def get_rehash_value(self, key: Any) -> int:
        return (self.get_hash_value(key) + 1) % self.capacity

    def search_bucket(self, key: Any) -> Any:
        hash = self.get_hash_value(key)
        bucket = self.table[hash]
        
        for _ in range(self.capacity):
            if bucket.status == Status.EMPTY:
                break
            elif bucket.status == Status.OCCUPIED and bucket.key == key:
                return bucket
            hash = self.get_rehash_value(hash)
            bucket = self.table[hash]

        return None

    def search(self, key: Any) -> Any:
        bucket = self.search_bucket(key)
        if bucket is not None:
            return bucket.value
        else:
            return None
    
    def add(self, key: Any, value: Any) -> bool:
        if self.search(key) is not None:
            return False
        
        hash = self.get_hash_value(key)
        bucket = self.table[hash]
        for _ in range(self.capacity):
            if bucket.status == Status.EMPTY or bucket.status == Status.DELETED:
                self.table[hash] = Bucket(key, value, status=Status.OCCUPIED)
                return True
            hash = self.get_rehash_value(hash)
            bucket = self.table[hash]
        return False
    
    def remove(self, key: Any) -> bool:
        bucket = self.search_bucket(key)
        if bucket is None:
            return False
        bucket.set_status(Status.DELETED)
        return True
    
    def dump(self) -> None:
        for i in range(self.capacity):
            bucket = self.table[i]
            print(f"{i:2}. ", end='')
            if bucket.status == Status.OCCUPIED:
                print(f"{bucket.key} ({bucket.value})")
            elif bucket.status == Status.EMPTY:
                print('-- 미등록 --')
            elif bucket.status == Status.DELETED:
                print('-- 삭제 완료 --')

hash = OpenHash(13)

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

