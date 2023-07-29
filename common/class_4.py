class ClassInstance:
    name='김현호'
    age=49

ci=ClassInstance()
print(ci.name)

class ClassInstance2:
    result=0
    name = '김현호'
    age = 49

    def __init__(self):
        self.result=2

    def __repr__(self):
        return 'repr'

cl1=cl1()

print(cl1)

"""
class cl2:

    def __init__(self,name,age,address):
        print('init')
        self.name=name
        self.age=age
        self.address=address
    def __del__(self):
        print('객체 소멸할때 ..')

 # 객체 기본 값 만들기
    def __repr__(self):
        return self.name

# 문자열이면 repr보다 우선
    def __str__(self):
        return 'call str !!'

cl2=cl2('김현호',49,'안산')


print(cl2.name)
print(cl2.age)
print(cl2.address)

print(cl2)
print(str(cl2))

print('{} 은 {} 입니다'.format('김현호',34))
print(f'{cl2.name} 나이는 {cl2.age} 주소는 {cl2.address}')
