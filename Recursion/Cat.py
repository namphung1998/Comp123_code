class Cat:
    def __init__(self, name, color, parent=None):
        self.catName = name
        self.parent = parent
        self.color = color
        self.children = []

    def makeChild(self):
        childNumber = len(self.getChildren())
        newName = self.catName+"-"+str(childNumber)
        newColor = self.color
        newCat = Cat(newName, newColor, self)
        self.children.append(newCat)
        return newCat

    def getParent(self):
        return self.parent

    def getChildren(self):
        return self.children

    def getName(self):
        return self.catName

    def getColor(self):
        return self.color

    def countAncestors(self):
        # use a counter
        count = 0
        theParent = self.parent
        # use a loop to while loop over the ancestors before them2
        # while we are tracking a cat
        while theParent != None:
            #add 1 to counter
            count = count + 1
            #look up that cat's parent
            theParent = theParent.getParent()
        return count
    def __repr__(self):
        return "<cat " + self.getName() + ">"

    def __str__(self):
        return "<cat "+self.getName()+">"

n = Cat("Nermal", "Gray")
print(n.getName())
print(n)
print(n.getColor())

n1 = n.makeChild()
print(n1)
print(n1.getParent())
print(n.getChildren())
print(n1.getColor())

n11 = n1.makeChild()
n12 = n1.makeChild()
n13 = n1.makeChild()
print(n1.getChildren())
print(n.getChildren())

print(n13.countAncestors())
print(n1.countAncestors())
print(n.countAncestors())