"""
기본 개념: 바로 옆 원소와 계속 비교하며 scan
개선 1. 원소 교환횟수가 0이면 정렬을 마친것으로 보고 종료
개선 2. 각 패스에서 비교/교환을 하다가 특정한 원소 이후부터 교환하지 않는다면,
        그 원소보다 앞쪽에 있는 원소들은 정렬을 마친 것으로 간주함.
        이후 패스에서는 스캔범위를 좁혀 진행
"""
def bubble_sorted(lst: list) -> list:
    n = len(lst)
    i = 0
    num = 1
    while i < n-1:
        exchanging = 0
        last = n-1
        print(f"{num}번 패스")
        for j in range(n-1, i, -1):
            for k in range(n-1):
                print(f"{lst[k]:2}{'    ' if k != j-1 else ' -- ' if lst[j-1] < lst[j] else ' <> '}", end='')
            print(f'{lst[n-1]:2}')
            if lst[j-1] > lst[j]: 
                lst[j-1], lst[j] = lst[j], lst[j-1]
                exchanging += 1
                last = j
        for k in range(n-1):
            print(f"{lst[k]:2}", end="    ")
        print(f"{lst[n-1]:2}")
        if not exchanging: break
        i = last
        num += 1

lst_1 = [1, 3, 9, 4, 7, 8, 6]

bubble_sorted(lst_1)