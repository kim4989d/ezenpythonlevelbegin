class static_1:


    def __init__(self):
        self.standvar='standvar'
        self.staticvar='staticvar'



    @staticmethod
    def statmethod():
        print('static method')
        #staticmethod에서는 self 을 접근할수 없다
        # print(self.staticvar)


    def standmethod(self):
        print('stand method')
        print(self.standvar)
stat=static_1()

# stat.statmethod()
stat.standmethod()

#클래스명.일반메소드는 반드시 객체을 넘겨주어야한다
static_1.standmethod(stat)
#staticmethod 메소드 이기때문에 클래스명.staticmethod 로 접근가능 객체를 넘길필요가 없다
static_1.statmethod()