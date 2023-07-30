from coding_1.parent_child.factory1 import factory1


class sell1(factory1):

    def sellice(self):
        print('sell...')


se1=sell1('베스킨라벤스','31가지맛',31,'공장1')
print(se1.currentcompany())
print(se1.currenticetype())
print(se1.currenticecount())
print(se1.currentfactorytype())
se1.commonmake()
