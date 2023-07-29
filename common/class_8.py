class staticclass:

    def instatncemethod(self, a, b):
        return a + b

    @classmethod
    def classmethod(cls, a, b):
        return a + b

    @staticmethod
    def staticmethod(a, b):
        return a + b


inst = staticclass()
print(inst.instatncemethod(1, 2))
print(inst.classmethod(1, 2))
print(inst.staticmethod(1, 2))
print('=' * 50)

print(staticclass.instatncemethod(None, 3, 4))

print(staticclass.instatncemethod(inst, 3, 4))
# instance 는 클래스명.메소드로 호출하면 앞에 객체나 None로 선언해야한다 아니면 오류 발생
# print(staticclass.instatncemethod(3, 4))

print('=' * 50)
# print(staticclass.classmethod(None, 3, 4))

# print(staticclass.classmethod(inst, 3, 4))
# classmethod 는 클래스 선언없이 입력해야 오류 발생하지않음

stob = staticclass()
print(staticclass.classmethod(3, 4))
# instance 로도 접근 가능
print(stob.classmethod(3, 4))


