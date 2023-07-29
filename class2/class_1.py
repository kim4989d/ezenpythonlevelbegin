class Room1304:

    # 객체가 생성되면 해당하는 인자가 init로 값이 들어온다
    # 생성자  메소드
    # self
    def __init__(self,name,age,address):
        self.name =name
        self.age = age
        self.address = address

        print(self.name)
        print(self.age)
        print(self.address)


    def home(self, name, age, address):
            self.name = name
            self.age = age
            self.address = address

            print(self.name)
            print(self.age)
            print(self.address)

#인자가 없는 생성자 ,기본 생성자
# r1304 = Room1304()
# r1304.home('김현호', 49, '양천구')

#인자가 있는 생성자
#인자가있는생성자가 오면 기본생성자를 쓰지 못한다
# r1304_2 = Room1304('아무개', 40, '스페인')
#
# print('===' * 50)
# r1304_3 = Room1304('나이팅게일', 30, '이탈리아')
































