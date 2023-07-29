# java 는 단일 상속만 가능하지만
# python은 다중상속도 가능


class superclass1:

    def class1method(self):
        print('class1 print')


class superclass2:

    def class2method(self):
        print('class2 print')


class childclass(superclass1,superclass2):

    def submethod(self):
        print('sub print')

print(childclass.mro())




