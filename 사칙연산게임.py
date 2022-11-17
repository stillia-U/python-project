from random import randrange
import sys

def question(template, answer):
    quiz=int(input(template))

    if quiz == answer:
        return True
    else:
        return False
def answer(first, type, second):
    if type == '덧셈':
        return first+second
    elif type == '뺄셈':
        return first-second
    elif type == '곱셈':
        return first*second
    elif type == '나눗셈':
        return first/second

print('사칙연산게임입니다. ai가 랜덤으로 문제를 낸 후 여러분이 맞추는 게임입니다.')
type_f=input('먼저, 어떤 연산을 할 것인지 정해주세요. (덧셈, 뺄셈, 곱셈, 나눗셈 형식으로 작성합니다.)')
size_f=int(input('그다음, 랜덤 숫자 범위를 정할 것 입니다. 가장 작은 범위를 먼저 정하세요. (1 이상 / 자연수만 입력해주세요.)'))
size_s=int(input('그다음, 가장 큰 범위를 정하세요. (10초과 / 자연수만 입력해주세요.)'))

type_s=None
if type_f == '덧셈':
    type_s = '+'
elif type_f == '뺄셈':
    type_s = '-'
elif type_f == '곱셈':
    type_s = '×'
elif type_f == '나눗셈':
    type_s = '÷'
else:
    print('제대로된 타입을 입력해주세요.')
    sys.exit()

print('기본 준비가 완료 되었습니다. ai가 이 정보에 따라 랜덤으로 다섯가지 문제를 제작합니다.')
ff=randrange(size_f, size_s, 1)
fb=randrange(size_f, size_s, 1)
sf=randrange(size_f, size_s, 1)
sb=randrange(size_f, size_s, 1)
tf=randrange(size_f, size_s, 1)
tb=randrange(size_f, size_s, 1)
of=randrange(size_f, size_s, 1)
ob=randrange(size_f, size_s, 1)
fif=randrange(size_f, size_s, 1)
fib=randrange(size_f, size_s, 1)

print('문제를 제작 완료하였습니다.')
quiz = [
    None,
    question('{}{}{}=?'.format(ff,type_s,fb), answer(ff, type_f, fb)),
    question('{}{}{}=?'.format(sf,type_s,sb), answer(sf, type_f, sb)),
    question('{}{}{}=?'.format(tf,type_s,tb), answer(tf, type_f, tb)),
    question('{}{}{}=?'.format(of,type_s,ob), answer(of, type_f, ob)),
    question('{}{}{}=?'.format(fif,type_s,fib), answer(fif, type_f, fib)),
]
answers='\n\n_채점_ \n'
i=0
for key in quiz:
    i+=1
    answers+='{} 번: '.format(i)
    if key:
        answers+='정답입니다!\n'
    else:
        answers+='오답입니다!\n'
print(answers)