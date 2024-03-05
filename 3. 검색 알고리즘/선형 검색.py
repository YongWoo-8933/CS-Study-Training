from typing import Any, Sequence

def sequential_search(arr: Sequence, key: Any) -> int:
    length = len(arr)
    for i in range(length):
        if arr[i] == key: 
            return i
    else:
        return -1

array = [6, 8, 11, 30, 42, 5, 29, 13]

while True:
    key = int(input("배열에서 찾을 값을 입력해주세요: "))
    index = sequential_search(arr=array, key=key)
    if index == -1: 
        print(f"{key}는 배열 안에 없는 값입니다.") 
    else: 
        print(f"{key}는 배열의 '{index}' 인덱스에 있습니다.")
    x = input("계속 찾으시겠습니까? (y: 계속, 다른 값 입력: 종료): ")
    if x == "y" or x == "Y": continue
    else: break