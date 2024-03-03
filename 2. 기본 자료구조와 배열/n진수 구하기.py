d = ""
dchar = "0123456789ABCDEF"

while True:
    n = int(input("n값을 입력해주세요(최대 16): "))
    if not 2 <= n <= 16: continue
    num = int(input("바꿀 값을 입력해주세요: "))

    while num:
        d = dchar[num % n] + d
        num //= n

    print(f"{n}진수로 변환된 값은 '{d}'입니다.")
    break
