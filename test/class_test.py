class Class_test:
    global glovar
    glovar='gloval'

    def __init__(self, test):
        self.test=test
        self.glovar='gloval2'

# ctest = Class_test()
ctest = Class_test('ok')
print(ctest.test)
print(ctest.glovar)

print(glovar)