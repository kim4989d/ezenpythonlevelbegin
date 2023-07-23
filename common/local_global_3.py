class Var4:
    # static 클래스 변수 :모든 객체에서 공3
    gname = '김현호 아무개'

    def gname2(self):
        # 해당하는 객체로 접근
        print(f'{self.gname} 객체 변수')
        # 전역으로 접근 (static)
        print(f'{Var4.gname}  static(전역) 변수')

        # return Var2.gname

    def gname3(self, name):
        self.gname = name
        return self.gname

    def gname4(self,name):
        Var4.gname = name
        return Var4.gname


# var2=Var2()
# print(var2.gname2())
var4 = Var4()
var4.gname2()
# 클래스명.변수 메소드 (객체)->해당하는객체를 넘긴다
Var4.gname2(var4)

var5 = Var4()
var5.gname3('이순신')
var5.gname2()

var5.gname4('광개토 대왕')
var5.gname2()
