#iter 이터레이터
# 해당하는데이터를 이터레이터로 바꾸면
# next 로 접근할수있다

class it_1:

    def itprint(self):
        a = 'abc'
        ait=iter(a)

        init=1
        while init<=len(a):
            print(next(ait))
            init=init+1

it=it_1()
it.itprint()