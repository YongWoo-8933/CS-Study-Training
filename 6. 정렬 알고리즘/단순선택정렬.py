"""
기본 개념: i번째 원소 ~ n번째 원소까지를 스캔해 가장 작은 원소를 맨앞으로 이동시킴
"""
def straight_selection_sorted(lst: list) -> list:
    n = len(lst)
    for i in range(n-1):
        m = i
        for j in range(i + 1, n):
            if lst[m] > lst[j]: m = j
        lst[i], lst[m] = lst[m], lst[i]
    return lst

lst_1 = [1, 3, 9, 4, 7, 8, 6]

print(straight_selection_sorted(lst_1))