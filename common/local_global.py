# global variable
#지역변수 :해당하는 메소드안에 변수를 선언하면 지역변수이다
#지역변수는 해당하는 메소드가 닫히면 값 변수가  소멸한다
#지역변수에 global 로 변수앞에 선언하면 지역변수 전역변수로
#같은 이름이 생긴다


class Var1:
    globalvar = 'gvar'

    def local(self):
        local = 'lvar'
        print(local)


    def local_global(self):
        global local_global
        local_global = 'local->global'
        self.local_global = 'global'
        print(self.local_global)

    print(globalvar)
    print(local_global)


var1 = Var1()
print(var1.globalvar)
print(var1.local_global)

var1.local_global()
# var1.local_global = 'ok'
print(f' {var1.local_global} local_global() 찍고 실행')

var2 = Var1()

var2.local()
var2.local_global()

