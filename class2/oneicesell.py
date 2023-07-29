from class2 import icefactory

class oneicesell(icefactory):

    def __init__(self,commanyname,icetype):
        self.commandyname=commanyname
        self.icetype=icetype
        print('init')

    def parentmethod(self):
        print(' oneicesell method')


oneice = oneicesell('베스킨라벤스','엄마는 외계인')

oneice.parentmethod()


