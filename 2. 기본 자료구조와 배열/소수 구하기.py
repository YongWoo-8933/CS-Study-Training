"""
기본 개념
1.   n이 소수라면 2부터 n-1까지 어떤 정수로도 나누어 떨어지지 않는다.
1-2. n이 소수라면 2부터 n-1까지의 어떤 소수로도 나누어 떨어지지 않는다.
1-3. n이 소수라면 n의 제곱근 이하 어떤 소수로도 나누어 떨어지지 않는다.
"""

prime_numbers = [2, 3]
counter = 0

for i in range(5, 1001, 2):
    j = 1
    while prime_numbers[j] * prime_numbers[j] <= i:
        counter += 2
        if not i % prime_numbers[j]: break
        j += 1
    else: 
        counter += 1
        prime_numbers.append(i)

print("1부터 1000까지의 소수는 다음과 같습니다.")
print(prime_numbers)
print(f"총 나눗셈 실행 횟수는 {counter}회 입니다.")