from random import randrange

print('숫자맞히기 게임입니다. 먼저, 컴퓨터가 1부터 100까지의 수 중, 한가지를 생각할 것 입니다.')
r=randrange(1,100,1)
answer=None
trys=0
while True:
    answer=int(input('컴퓨터가 생각한 숫자를 맞춰보세요.'))
    if answer==r:
        trys+=1
        break
    elif answer > r:
        print('컴퓨터가 생각한 숫자보다 작습니다!')
        trys+=1
    elif answer < r:
        print('컴퓨터가 생각한 숫자보다 큽니다!')
        trys+=1
    else:
        print('error')

print('정답입니다!', trys,'번 시도하셨습니다!')