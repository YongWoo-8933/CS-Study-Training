"""
기본 개념: 카드를 정리하듯 주목한 원소를 알맞은 위치에 삽입
"""
def straight_insertion_sortied(lst: list) -> list:
    n = len(lst)
    for i in range(1, n):
        temp = lst[i]
        for j in range(i-1, -1, -1):
            if lst[j] > temp: 
                lst[j+1] = lst[j]
            else:
                lst[j+1] = temp
                break
    return lst

lst_1 = [1, 3, 9, 4, 7, 8, 6]

print(straight_insertion_sortied(lst_1))