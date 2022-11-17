def computer(type, once, twice):
    if type == 'add':
        return once+twice
    elif type == 'sub':
        return once-twice
    elif type == 'mul':
        return once*twice
    elif type == 'div':
        return once/twice

print('python 사칙연산 계산기입니다.')
information = input('먼저, 어떤 연산을 할 것인지 입력해주세요. (덧셈, 뺄셈, 곱셈, 나눗셈으로 작성해주세요.)')
type = None
sign = None
bk = True

if information == '덧셈':
    type = 'add'
    sign = '+'
    print('이제 첫번째 더할 값과 두번째 더할 값을 각각 정합니다.')
elif information == '뺄셈':
    type = 'sub'
    sign = '-'
    print('이제 첫번째 뺄 값과 두번째 뺄 값을 각각 정합니다.')
elif information == '곱셈':
    type = 'mul'
    sign = '×'
    print('이제 첫번째 곱할 값과 두번째 곱할 값을 각각 정합니다.')
elif information == '나눗셈':
    type = 'div'
    sign = '÷'
    print('이제 나누어지는 수와 나누는 수를 각각 정합니다.')
else:
    print('값을 제대로 입력해주세요.')
    bk = False

if bk:
    once=int(input('첫번째 값은 무엇인가요?'))
    twice=int(input('두번째 값은 무엇인가요?'))
    print('{}{}{}={}'.format(once, sign, twice, computer(type, once, twice)))