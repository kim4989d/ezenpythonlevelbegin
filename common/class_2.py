class Test1:

    def Test(self,input):
        return input
    class InnerTest:

        def Test2(self,input):
            return input


test1=Test1()
test1=test1.Test('test1')
print(test1)


test2=Test1.InnerTest()
test2me=test2.Test2('test2')
print(test2me)

