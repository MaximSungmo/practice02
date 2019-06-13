# 문제4 반복문을 이용하여 369게임에서 박수를 쳐야 하는 경우의 수를 순서대로 화면에 출력해보세요. 1부터 99까지만 실행하세요.

min = 1
max = 100
*numbers, = range(min, max+1)
conditions = (3, 6, 9)
print(numbers)

for number in numbers:
    clap_count = 0
    i = number
    flag = True
    while(flag):
        if i%10 in conditions:
            clap_count += 1
        if i < 10:
            if clap_count > 0:
                print(number, '짝'*clap_count)
            flag = False
        i = i // 10








