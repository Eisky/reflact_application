class province(object):
    memo = 'one of China '

    def __init__(self, name, capital, leader, dork):
        self.name = name
        self.capital = capital
        self.leader = leader
        self.__belonging = dork

    def sportsmeeting(self):
        print self.name, 'implenment sports meeting'

    def anticorruption(self):
        print self.leader, 'was punished due to corruption'

    def capitalset(self):
        print self.capital, 'was set to be capital'

    @staticmethod
    def purify():
        print 'If you feel tired, just have a break'

    # readonly
    @property
    def visit(self):
        print "I'm visiting", self.name + '.'


    def judge(self):
        print self.__belonging


hn = province('henan', 'zhengzhou', 'sunki', 'good')
hb = province('hebei', 'shijiazhuang', 'demi', 'great')
japan = province('japan', 'China', 'yuki', 'sb')

print hn.name
print hb.capital
print province.memo
print hb.sportsmeeting()
print hn.sportsmeeting()
print hn.anticorruption()
print hb.anticorruption()
print hb.capitalset()
print hn.capitalset()
print province.purify()
print hn.visit
print hb.visit
print japan.judge()
