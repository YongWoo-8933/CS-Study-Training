"""
기본 개념: 정렬할 배열의 원소를 그룹으로 나누고 각 그룹별로 정렬.
=> h값의 수열은 그룹들이 서로 겹치지 않게 하는게 좋음. 즉 h값들이 서로 배수관계가 되지 않도록 함.
=> ex) 수열을 3i+1로 하고, 초기 h값을 n//9를 넘지 않도록 함.
"""
def shell_sorted(lst: list) -> list:
    n = len(lst)
    h = 1
    while h < n // 9:
        h = h * 3 + 1

    while h > 0:
        for i in range(h, n):
            j = i - h
            temp = lst[i]
            while j >= 0 and lst[j] > temp:
                lst[j + h] = lst[j]
                j -= h
            lst[j+h] = temp
        h //= 3
    return lst

lst_1 = [1, 3, 9, 4, 11, 7, 88, 8, 6]

print(shell_sorted(lst_1))