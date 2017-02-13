class Cat():
    def __init__(self, inName, parent = None):
        self.name = inName
        self.parent = parent
        self.children = []

    def getName(self):
        return self.name

    def getParent(self):
        return self.parent

    def getChildren(self):
        return self.children

    def makeChild(self):
        childNum = len(self.getChildren())
        newCatName = self.name+ "-" + str(childNum)
        newCat = Cat(newCatName, self)
        self.children.append(newCat)
        return newCat

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return "<Cat "+self.getName()+">"

c = Cat("Garfield")
print(c.getName())
print(c)
print(str(c))

g2 = c.makeChild()
print(g2)
print(g2.getParent())
print(c.getChildren())

