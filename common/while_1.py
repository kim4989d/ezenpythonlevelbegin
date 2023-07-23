init=0




while init<=10:
    print(init)
    init=init+1




while  True:

    inp= int(input())


    print('=' * 50)

    print('1. 추가 ')
    print('2. 삭제 ')
    print('3. 검색 ')
    print('4. 나가기 ')

    print('=' * 50)

    if inp==1:
            print(inp,' 1')
    if inp==2:
            print(inp,' 2')
    if inp == 3:
        print(inp,' 3')
    if inp == 4:
        print(inp,' 4')
        exit()