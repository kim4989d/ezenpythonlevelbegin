from abc import ABCMeta, abstractmethod


# 추상클래스는 추상메소드를 가지면 객체생성을 할수없다
# 추상메소드가 없으면 일반적인 클래스로 객체생성가능


# 아이스크림을 회사에서 납품 받고공장으로 지시
# 공장에서 대리점으로 납품
#
# 회사이름,아이스크림종류,아이스크림 갯수 ,공장종류:공장1_공장2


#대리점은 기본 아이스크림 최종부모에 가서 필수적인 정보를 받아오고 아이스크림을 납품받아서 판매한다
class baseice(metaclass=ABCMeta):

    def __init__(self,companyname,icetype,icecount,factorytype):
        self.companyname=companyname
        self.icetype=icetype
        self.icecount=icecount
        self.factorytype=factorytype

    def currentcompany(self):
        return self.companyname

    def currenticetype(self):
        return self.icetype
    def currenticecount(self):
        return self.icecount
    def currentfactorytype(self):
        return self.factorytype
    #각공장에서는 회사별 아이스크림을 만든다

    @abstractmethod
    def commonmake(self):
        pass