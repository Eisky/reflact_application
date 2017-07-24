class A:
    def __init__(self):
        pass

    def save(self):
        print 'save from A'


class B:
    def __init__(self):
        pass


class C:
    def __init__(self):
        pass

    def save(self):
        print 'save from c'


class D(B, C):
    def __init__(self):
        pass


a = D()
print a.save()
