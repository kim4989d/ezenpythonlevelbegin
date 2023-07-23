

class Class1:
    name='김현호'
    def ClassMethod(self):
        print('classmethod')


class Class2(Class1):

    def __init__(self,name):
        self.name=name


    def Class2Method(self):
        print('class3method')

class2=Class2()
class2.Class2Method()
class2.ClassMethod()

