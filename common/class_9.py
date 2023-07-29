class clsclass:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    @classmethod
    def classmethod(cls, a, b):
        return cls(a, b)

    def sum(self):
        print(self.a+self.b)

order=clsclass(3,4)
order.sum()

order2=clsclass.classmethod(1,2)
order2.sum()