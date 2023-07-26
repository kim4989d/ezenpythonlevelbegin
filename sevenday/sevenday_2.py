# dictionary input key value 데이타 입력 name 이름
# {'name:':'김현호','name':'이순신'}

di = {}
i = 0

while True:
    inputvalue = input('이름을 입력하시오')
    i = i + 1
    if inputvalue == 'q':
        exit()

    di.setdefault(i, inputvalue)
    print(di)