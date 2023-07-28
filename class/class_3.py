class Calu2:

    def __init__(self):
        # 전역변수
        self.result=0
    def add(self,num):
        self.result=self.result+num

    def printtotal(self):
        print(self.result)

    def sub(self,num):
        self.result=self.result-num
        print(f'합{self.result}')

cal=Calu2()
cal.add(10)
cal.add(10)
cal.add(10)

cal.sub(10)
# cal.printtotal()


