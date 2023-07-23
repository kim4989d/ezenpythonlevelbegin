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



ci=ClassInstance()
print(ci.name)
print(ci.age)
# print(ci.result)

