# 가변 변수:인자갯수에 상관없이 받을수있다
#메소드는 오버로딩을 할수없다(python)


def VarMethod1(*args):
    print(args)


def VarMethod2(*args):

    for i in args:
        print(i)


# 가변변수는 일반변수앞에 올수 없다
def VarMethod3(name,*args):
    print(name)
    print(args)

def VarMethod4(input,**args):
    print(input)
    print(args)

def VarMethod5(arg1,arg2,**args):
    print(arg1)
    print(arg2)
    print(args)

def VarMethod6(*args,name):
    print(args)
    print(name)


VarMethod1(1,2,3,'문자1')
VarMethod2(1,2,3,'문자1','문자2')
VarMethod3('김현호',1,2,3,4,5,'문자1')
VarMethod4('김현호',name='김현호',age='49')
VarMethod5('김현호',49,name='김현호',age='49')
# VarMethod6(1,2,3,4,'변수')







