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
    def printroom():
        while True:
            inputvalue = input('룸번호 룸타입  룸 인원을 입력하세요 ex)room1301/html/5 \n')
            sp = inputvalue.split('/')
            if len(sp) != 3:
                print("세자리를 입력 !!")
            else:
                for i in sp:
                    room.append(i)

                schob = school(room[0], room[1], room[2])
                obinput.append(schob)

                for i in obinput:
                    print('=' * 100)
                    school.printe(f'룸번호:{i.roomnumber}')
                    school.printe(f'룸타입:{i.roomtype}')
                    school.printe(f'룸인원:{i.roomcheck}')
                    print()
                    print('=' * 100)

                room.clear()


school.printroom()
