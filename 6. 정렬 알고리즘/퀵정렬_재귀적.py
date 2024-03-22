"""
기본 개념: pivot값을 기준으로 pointer left, right로 나눠 스캔하며 그루핑
=> pivot을 어떻게 설정하느냐가 정렬의 성능에 영향을 미침.
=> 배열의 중앙값을 pivot으로 삼아 재귀적으로 구현한 방식
"""
def qsort(lst: list, left: int, right: int) -> None:
    pointer_left = left
    pointer_right = right
    pivot = lst[(left + right) // 2]

    print(f"list[{left}] ~ list[{right}]:", *lst[left: right + 1])

    while pointer_left <= pointer_right:
        while lst[pointer_left] < pivot: pointer_left += 1
        while lst[pointer_right] > pivot: pointer_right -= 1
        if pointer_left <= pointer_right:
            lst[pointer_left], lst[pointer_right] = lst[pointer_right], lst[pointer_left] 
            pointer_left += 1
            pointer_right -= 1
    
    if left < pointer_right: qsort(lst, left, pointer_right)
    if right > pointer_left: qsort(lst, pointer_left, right)


def quick_sorted(lst: list) -> list:
    qsort(lst, 0, len(lst) - 1)
    return lst


lst_1 = [1, 3, 9, 94, 82, 4, 11, 77, 7, 88, 8, 104, 6]

print(quick_sorted(lst_1))