from typing import Any, Sequence
import copy

def sequential_search(arr: Sequence, key: Any) -> int:
    new_arr = copy.deepcopy(arr)
    new_arr.append(key)
    i = 0
    while True:
        if new_arr[i] == key: break
        i += 1
    return -1 if i == len(arr) else i

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