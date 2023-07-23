class Var2:
#static 클래스 변수 :모든 객체에서 공유
    gname='김현호 아무개'

    def gname2(self):
        # print(f'{self.gname} 객체 변수')
        print(f'{Var2.gname}  static(전역) 변수')

        # return Var2.gname

# var2=Var2()
# print(var2.gname2())
var2=Var2()
var2.gname2()

var3=Var2()
var3.gname2()


class Var3:
#static 클래스 변수 :모든 객체에서 공3
    gname='김현호 아무개'

    def gname2(self):
        print(f'{self.gname} 객체 변수')
        print(f'{Var3.gname}  static(전역) 변수')

        # return Var2.gname

# var2=Var2()
# print(var2.gname2())
var3=Var3()
var3.gname2()

var3=Var3()
var3.gname2()
