# 문제5. 함수 sum 을 만드세요. 이 함수는 임의의 개수의 인수를 받아서 그 합을 계산합니다.

def sum(*nums):
    result=0
    for num in nums:
        result += num
    return result

print(sum())
print(sum(1, 2))
print(sum(3, 4, 5, 6))

