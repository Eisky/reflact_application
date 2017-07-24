class test1:
    def __init__(self):
        self.__name = 'sunki'

    @property
    def fun(self):
        return self.__name


class test2(object):
    def __init__(self):
        self.__name = 'sunki'


    def fun1(self):
        return self.__name


t1 = test1()
print t1.fun
t1.fun = 'demi'
print t1.fun
t2 = test2()
print t2.fun1
t2.fun1 = 'yuki'
print t2.fun1