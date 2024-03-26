"""
기본 개념: 누적 도수분포표를 만들고, 표의 인덱스에따라 재배치
"""
def counting_sorted(lst: list) -> list:
    M = max(lst)
    n = len(lst)
    f = [0] * (M + 1)
    new_lst = [0] * n
    
    for i in range(n): f[lst[i]] += 1
    for i in range(1, M+1): f[i] += f[i-1]
    for i in range(n-1, -1, -1): f[lst[i]] -= 1; new_lst[f[lst[i]]] = lst[i]

    return new_lst


lst_1 = [1, 3, 9, 4, 11, 7, 88, 8, 6]

print(counting_sorted(lst_1))