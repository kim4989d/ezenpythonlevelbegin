
if 'abc' not in 'abc':
    print('true')
else:
    print('false')



if 2 == 2 and 'kkk' not in 'abc':
    print('if문 실행')
else:
    print('else문 실행')

# 출력값: if문 실행

if 5 == 1 and 'kkk' not in 'abc':
    print('if문 실행')
else:
    print('else문 실행')

# 출력값: else문 실행

if 5 == 1 or 'kkk' not in 'abc':
    print('if문 실행')
else:
    print('else문 실행')

# 출력값: if문 실행

if not 5 == 1:
    print('if문 실행')
else:
    print('else문 실행')

# 출력값: if문 실행

if 1 == 1 and 2 == 2 and 3 == 3:
    print('if문 실행')
else:
    print('else문 실행')

# 출력값: if문 실행


if 3 is 3.0:
    print('if문 실행')
else:
    print('else문 실행')

# 출력값: else문 실행




a = []
b = []
c = a

result = (a is b)
print("a is b ?", result)

result = (a is c)
print("a is c ?", result)

result = (b is c)
print("b is c ?", result)