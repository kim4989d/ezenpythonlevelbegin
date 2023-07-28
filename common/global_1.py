class school:


    def __init__(self, roomnumber, roomtype, roomcheck):
        self.roomnumber = roomnumber
        self.roomtype = roomtype
        self.roomcheck = roomcheck

    @staticmethod
    def printok():
        a = []
        obinput=[]
        while True:
            inputvalue = input('룸번호 룸타입  룸 인원을 입력하세요 ex)room1301/html/5')
            sp = inputvalue.split('/')

            for i in sp:
                a.append(i)

            schob = school(a[0], a[1], a[2])
            obinput.append(schob)

            for i in obinput:
                print(i.roomnumber)
                print(i.roomtype)
                print(i.roomcheck)

            a.clear()
school.printok()
