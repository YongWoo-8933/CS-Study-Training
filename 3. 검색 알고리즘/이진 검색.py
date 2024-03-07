from typing import Any, Sequence

def binary_search(arr: Sequence, key: Any) -> int:
    pointer_left = 0
    pointer_right = len(arr) - 1
    while True:
        pointer_center = (pointer_left + pointer_right) // 2
        if arr[pointer_center] == key:
            return pointer_center
        elif arr[pointer_center] < key:
            pointer_left = pointer_center + 1
        elif arr[pointer_center] > key:
            pointer_right = pointer_center - 1
        if pointer_left > pointer_right: break
    return -1

array = [6, 8, 11, 30, 42, 58, 69, 71, 90, 98, 105, 107, 129]

while True:
    key = int(input("배열에서 찾을 값을 입력해주세요: "))
    index = binary_search(arr=array, key=key)
    if index == -1: 
        print(f"{key}는 배열 안에 없는 값입니다.") 
    else: 
        print(f"{key}는 배열의 '{index}' 인덱스에 있습니다.")
    x = input("계속 찾으시겠습니까? (y: 계속, 다른 값 입력: 종료): ")
    if x == "y" or x == "Y": continue
    else: break