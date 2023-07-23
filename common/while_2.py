home={'name':'김현호','age':50,'address':'안산'}

person={}
i=0
while True:
    i=i+1
    inputvalue=input('이름을 입력하세요')
    if inputvalue == 'q':
        exit()

    person.setdefault(i,inputvalue)
    print(person)





