class HumanBeing(object):
    def __init__(self, name, age, job, grade,graudate):
        self.name = name
        self.age = age
        self.job = job
        self.grade = grade
        self.graudate = True

    def school(self):
        if self.grade >= 80:
            print "go to college"
        else:
            print "cannot go to college"

class Lilei(HumanBeing):
    def __init__(self,job):
        self.job = 'lawyer'

    def struggle(self):
        return self.job
        print 'being ceo'
        print "buy anything he wants"
class Hanmeimei(HumanBeing):
    def __init__(self):
        pass
    def school(self):
        return "break up with Lilei and get a new bf"
    def gotdumped(self):
        print 'got dumped by bf and wants to be with Lilei'

a = HumanBeing('sunki', '18','CS','81',True)
print a.school()
b = Lilei('lawyer')
print b.struggle()
c = Hanmeimei()
print c.gotdumped()
