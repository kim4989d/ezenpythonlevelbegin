# 추상클래스 ,추상 메소드 import 불러오기

from abc import ABCMeta,abstractmethod

# 추상클래스 ABCMeta
# 추상클래스는 겍채(instance)을 생성할수없다 메모리에 올라가지 못한다
# 단 자식을 통해서는 접근할수있다


# 추상클래스
# class interface_1(metaclass=ABCMeta):
#일반 클래스
class interface_1:

        def test(self):
            print('test')

        @abstractmethod
        def abstractmethod(self):
            pass

# 추상클래스이기때문에 객체생성을 할수없다
interface=interface_1()
interface.test()

class childone(interface_1):
    def abstractmethod(self):
        print('추상메소드입니다.')


child1=childone()
child1.abstractmethod()