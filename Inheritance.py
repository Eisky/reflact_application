class Father:
    def __init__(self):
        pass

    def Good(self):
        print "He's a good father"

    def Bad(self):
        print 'He is addicted to alcohol'


class Son(Father):
    def __init__(self):
        pass

    def Study(self):
        print 'Top student'

    def Bad(self):
        Father.Bad(self)
        print 'So he is son'


a = Father()
print a.Bad()
b = Son()
print b.Bad()
