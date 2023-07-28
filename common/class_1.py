class Class1:

    def Ok(self,input):
        return input


class Class2:

    def Ok(self,input):
        return "class2"+input


class Class3:

    def Test(self):
        print('test')


class1=Class1()
ok= class1.Ok('test')


class2=Class2()
ok=class2.Ok('test')


class3= Class3()
class3.Test()


class Class4:

    def Class4(self):
        print('class4')

class4=Class4()

