"""
기본 개념: 정렬할 배열을 두 그룹으로 나누고, 각 그룹 원소를 비교하고 새로운 배열에 저장하며 정렬.
=> 각 그룹의 원소 수가 1개가 될 때까지 나누는 과정을 재귀적으로 반복
"""
def _merge_sorted(lst_l: list, lst_r: list) -> list:
    pointer_l, pointer_r, pointer = 0, 0, 0
    n_l, n_r = len(lst_l), len(lst_r)
    lst = [0]*(n_l + n_r)

    if n_l > 1:
        lst_l = _merge_sorted(lst_l[:n_l//2], lst_l[n_l//2:])
    if n_r > 1:
        lst_r = _merge_sorted(lst_r[:n_r//2], lst_r[n_r//2:])
    
    while pointer_l < n_l and pointer_r < n_r:
        if lst_l[pointer_l] <= lst_r[pointer_r]:
            lst[pointer] = lst_l[pointer_l]
            pointer_l += 1
        else:
            lst[pointer] = lst_r[pointer_r]
            pointer_r += 1
        pointer += 1

    while pointer_l < n_l:
        lst[pointer] = lst_l[pointer_l]
        pointer_l += 1
        pointer += 1

    while pointer_r < n_r:
        lst[pointer] = lst_r[pointer_r]
        pointer_r += 1
        pointer += 1

    return lst


def merge_sorted(lst: list) -> list:
    n = len(lst)
    return _merge_sorted(lst[:n//2], lst[n//2:])

lst_1 = [1, 3, 9, 4, 11, 7, 88, 8, 6]

print(merge_sorted(lst_1))