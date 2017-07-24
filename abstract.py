from abc import ABCMeta, abstractmethod


class Alert:
    __metaclass__ = ABCMeta

    @abstractmethod
    def Send(self):
        pass


class Foo(Alert):
    def __init__(self):
        print '__init__'

    def Send(self):
        print 'abc'


t = Foo()
print t.Send()
