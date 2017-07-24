class foo:
    def __init__(self):
        return

    def foo1(self):
        print 'you are smart'

    def foo2(self):
        return

    def __call__(self):
        print 'Believe in yourself'


t = foo()
print t.foo1()
print t()
