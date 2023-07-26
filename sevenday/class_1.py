result = 0


def num(input):
    global result
    result = input
    return result


print(num('입력'))


class room1304:
    # self 현재 해당하는 객체(instance)
    def name(self):
        return 'self 객체'

    # 객체지향은 큰데에서 작은데로 간다
    # 지구.대한민국.서울.강남구.w.13.1304.김현호
    # 김현호.1304.13.w건물.
    def prname(self, name):
        print(f'이름은 {name} 입니다 ')


r1304 = room1304()
print(r1304.name())
r1304.prname('김현호')

r1304_2 = room1304()
r1304_2.prname('아무개')


# print(id(r1304))
# print(id(r1304_2))

# class :python1304

# 1 번객체 1 ~ 10 합을 출력하는메소드 sum1 출력 return
# 2 번객체  11 ~ 20 합을 출력하는메소드 sum2 출력 print

class python1304:

    def sum(self):
        result = 0

        for i in range(1, 11):
            result = result + i
        self.result = result
        return self.result

r1304 = python1304()
print(r1304.sum())


