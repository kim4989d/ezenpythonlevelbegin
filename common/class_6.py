class superclass:

    def supermethod(self):
        print('super method ')

    def overmethod(self):
        print('super over')


class subclass(superclass):

    def submethod(self):
        print('child method ')


    def overmethod(self):
        print('child over')


subob = subclass()
subob.supermethod()
subob.submethod()
subob.overmethod()

pare=superclass()
pare.supermethod()
