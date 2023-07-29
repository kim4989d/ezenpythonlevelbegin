class school:
    global room
    room = []
    global obinput
    obinput = []

    @staticmethod
    def printe(input):
        print(input, end="\t")

    def __init__(self, roomnumber, roomtype, roomcheck):
        self.roomnumber = roomnumber
        self.roomtype = roomtype
        self.roomcheck = roomcheck

    @staticmethod
    def listroom():
        for i in obinput:
            print('=' * 100)
            school.printe(f'룸번호:{i.roomnumber}')
            school.printe(f'룸타입:{i.roomtype}')
            school.printe(f'룸인원:{i.roomcheck}')
            print()
            print('=' * 100)

        room.clear()

    @staticmethod
    def updateroom():
        obinit = 0
        while True:
            inputvalue = input('수정할 룸번호 룸타입  룸 인원을 입력하세요 ex)room1301/html/5 \n')
            sp = inputvalue.split('/')
            if len(sp) != 3:
                print("세자리를 입력 !!")
            else:

                for i in obinput:
                    print('=' * 100)

                    if i.roomnumber == sp[0]:
                        i.roomnumber = sp[0]
                        i.roomtype = sp[1]
                        i.roomcheck = sp[2]
                        school.printe(f'룸번호:{i.roomnumber}')
                        school.printe(f'룸타입:{i.roomtype}')
                        school.printe(f'룸인원:{i.roomcheck}')
                        print()
                        print('=' * 100)
                        obinput[obinit] = i
                        obinit = obinit + 1

    @staticmethod
    def inputroom():
        inputvalue = input('룸번호 룸타입  룸 인원을 입력하세요 ex)room1301/html/5 \n')
        sp = inputvalue.split('/')
        if len(sp) != 3:
            print("세자리를 입력 !!")
        else:
            for i in sp:
                room.append(i)

            schob = school(room[0], room[1], room[2])
            obinput.append(schob)

    @staticmethod
    def roomprint():
        while True:
            print('============================================================')
            print('1. 리스트 ')
            print('2. 수정 ')
            print('3. 지우기  ')
            print('4. 입력 ')
            print('5. 나가기 ')

            print('============================================================')
            inputvalue = input()
            if inputvalue == '1':
                school.listroom()
            elif inputvalue == '2':
                school.updateroom()
            elif inputvalue == '3':
                print('지우기')
            elif inputvalue == '4':
                school.inputroom()
            elif inputvalue == '5':
                exit()



school.roomprint()