#문제6 숨겨진 카드의 수를 맞추는 게임입니다. 1-100까지의 임의의 수를 가진 카드를 한 장 숨기고 이 카드의 수를 맞추는 게임입니다. 아래의 화면과 같이 카드 속의 수가 57인 경우를 보면 수를 맞추는 사람이 40이라고 입력하면 "더 높게", 다시 75이라고 입력하면 "더 낮게" 라는 식으로 범위를 좁혀가며 수를 맞추고 있습니다. 게임을 반복하기 위해 y/n이라고 묻고 n인 경우 종료됩니다.

import random




# 게임 시작
print("수를 결정하였습니다. 맞추어 보세요 \n {0}-{1}".format(min,max))
counter = 1
exit_game = True
while(exit_game):
    # 초기 선언
    flag = True
    # 1 ~ 100 랜덤
    max, min = 100, 1
    n = random.randrange(max) + min
    print(n)

    while(flag):
        num = input('{0}>>'.format(counter))
        num = int(num)
        if n != num:
            if n < num:
                print('더 낮게')
            else :
                print('더 높게')

        else :
            choice = input('맞았습니다. \n다시 하시겠습니까?(y/n)>>')
            if choice == 'n':
                flag = False
                exit_game = False
            elif choice == 'y':
                counter = 0
                flag = False
            else :
                print('제대로 된 입력해주세요')
        counter += 1



