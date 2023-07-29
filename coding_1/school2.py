class commice:
    def __init__(self, company, factorytype, selltype, icetype):
        self.company = company
        self.factorytype = factorytype
        self.selltype = selltype
        self.icetype = icetype
        print('commice init')
    def Factorytype(self):
        return self.factorytype

    def Selltype(self):
        return self.selltype

    def Icetype(self):
        return self.icetype

    def Company(self):
        print('commonice com')
        return self.company


class factory(commice):

    def __init__(self, company, factorytype, selltype, icetype):
        self.company = company
        self.factorytype = factorytype
        self.selltype = selltype
        self.icetype = icetype
        print('factory init')

    def Factorytype(self):
        return self.factorytype

    def Selltype(self):
        return self.selltype

    def Icetype(self):
        return self.icetype

    def Company(self):
        print('factory com')
        return self.company


class sell1(factory):

    def __init__(self, company, factorytype, selltype, icetype):
        self.company = company
        self.factorytype = factorytype
        self.selltype = selltype
        self.icetype = icetype
        print('sell1 init')
    def Factorytype(self):
        return self.factorytype

    def Selltype(self):
        return self.selltype

    def Icetype(self):
        return self.icetype

    def Company(self):
        super().Company()
        print('sell com')
        
        return self.company


    def  Add(self):
        print('add')

# company, factorytype, selltype, icetype
sell = sell1('베스키라벤스', '공장1', '대리점1', '엄마는외계인')
print(sell.Company())
sell.Add()
# print(sell.icetype())
# print(sell.factorytype)
# print(sell.selltype())
print('=' * 100)
sell2 = commice('베스키라벤스2', '공장2', '대리점2', '엄마는외계인2')

# sell1(sell2)
#sell1=sell2  변환이 않됨

print(sell2.Company())
print(sell.Company())

print(type(sell))
print(type(sell2))
