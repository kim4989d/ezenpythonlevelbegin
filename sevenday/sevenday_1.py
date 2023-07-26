a = 1


def vartest():
    # global a
    b = 0
    result = b + 1
    global a
    a = result

   #dictionary input key value 데이타 입력 name 이름
# {'name:':'김현호','name':'이순신'}
# 출력 검색


print(a)
vartest()
