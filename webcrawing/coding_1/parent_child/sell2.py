from coding_1.parent_child.factory2 import factory2

class sell2(factory2):


    def sellice(self):
        print('sell ice...')



sel2=sell2('보노보노회사','보노아이스크림',10,'공장2')

print(sel2.currentcompany())
print(sel2.currenticetype())
print(sel2.currenticecount())
print(sel2.currentfactorytype())
sel2.commonmake()
