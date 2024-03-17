"""
아이디어
배열에 퀸의 위치를 저장하고 분기 조건을 따져가며 알고리즘 전개
열/행/대각선 중복여부를 따져 분기한정법 진행
"""
row_positions = [0] * 8
column_checker = [0] * 8
diagonal_checker_1 = [0] * 15
diagonal_checker_2 = [0] * 15

def set(i: int) -> None:
    for j in range(8):
        if  not column_checker[j] \
        and not diagonal_checker_1[i+j] \
        and not diagonal_checker_2[i-j + 7]:
            row_positions[i] = j
            if i == 7:
                for y in range(8):
                    for x in range(8):
                        print('■' if row_positions[x] == y else '□', end='')
                    print()
                print()
            else:
                column_checker[j] = diagonal_checker_1[i+j] = diagonal_checker_2[i-j + 7] = 1
                set(i+1)
                column_checker[j] = diagonal_checker_1[i+j] = diagonal_checker_2[i-j + 7] = 0

set(0)