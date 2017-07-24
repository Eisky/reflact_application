class Person:
    def __init__(self, name, gene, weight):
        self.name = name
        self.__gene = gene
        self.weight = weight
        self.age = None

    def talk(self):
        print 'I AM SUNKI'

    def fight(self, value):
        if value < self.weight:
            print "GO"
        else:
            print 'RUN'


people1 = Person('yuki', 'DNA', 100)
people1.age = 18
