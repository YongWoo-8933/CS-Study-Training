"""
기본 개념: 정렬할 배열을 힙으로 만들고, 힙에서 루트값을 순서대로 나열하는 식으로 정렬 진행
"""
def make_heap(lst: list) -> list:
    temp = lst[0]
    
    n = len(lst)
    parent = 0
    while parent < n//2:
        child_l = parent * 2 + 1
        child_r = child_l + 1
        child = child_r if child_r < n and lst[child_r] > lst[child_l] else child_l
        if temp >= lst[child]:
            break
        lst[parent] = lst[child]
        parent = child
    lst[parent] = temp

    return lst


def heap_sorted(lst) -> list:
    n = len(lst)

    for i in range((n-1)//2, -1, -1):
        lst[i:n] = make_heap(lst[i:n])

    for i in range(n-1, 0, -1):
        lst[0], lst[i] = lst[i], lst[0]
        lst[0:i] = make_heap(lst[0:i])

    return lst


lst_1 = [1, 3, 9, 4, 11, 7, 88, 8, 6]

print(heap_sorted(lst_1))