"""
아이디어
- 어떤 형태의 탑이더라도 맨 아래 1개층과 나머지 부분으로 이루어져있다고 가정
- 이 관점에서 재귀적으로 탑을 이동시킴
"""
def move(num: int, start: int, target: int) -> None:
    if num > 1:
        move(num-1, start, 6-start-target)
    
    print(f"원반 {num}을(를) {start}에서 {target}으로 옮깁니다.")

    if num > 1:
        move(num-1, 6-start-target, target)

n = int(input("하노이의 탑 층수를 입력해주세요: "))

move(n, 1, 3)
    