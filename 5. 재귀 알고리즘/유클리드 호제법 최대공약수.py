def greatest_common_divisor(x: int, y: int) -> int:
    a, b = (x, y) if x > y else (y, x)
    if b:
        return greatest_common_divisor(b, a % b)
    else:
        return a
    
print(f"36과 72의 최대공약수는 {greatest_common_divisor(36, 72)}입니다.")
print(f"36과 48의 최대공약수는 {greatest_common_divisor(36, 48)}입니다.")
print(f"108과 24의 최대공약수는 {greatest_common_divisor(108, 24)}입니다.")
print(f"27과 72의 최대공약수는 {greatest_common_divisor(27, 72)}입니다.")
print(f"18과 45의 최대공약수는 {greatest_common_divisor(18, 45)}입니다.")