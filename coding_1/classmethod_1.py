class classmethod_1:

    def __init__(self, one, two, three):
        self.one = one
        self.two = two
        self.three = three

    @classmethod
    def classmethod(cls):
        return cls(1, 2, 3)
    def contrmethod(self):
        print('stand method')
        print(self.one)
        print(self.two)
        print(self.three)



    # classmethod을 선언하면 해당하는 클래스 겍체을 호출 cls




clme=classmethod_1(4,5,6)
# clme.contrmethod()

clme.contrmethod()

clme2=clme.classmethod()
clme2.contrmethod()

