###Part 3
class MyClass:
    def __init__(self, pre, nTimes):
        self.prefix = pre
        self.nTimes = nTimes

    def echo(self, word):
        for i in range(self.nTimes):
            print(self.prefix, word)

t = MyClass("echo: ",3)
t.echo("happy")

y = MyClass("color", 2)
y.echo("purple")

###Part 4
class Adder:
    def __init__(self, startingValue):
        self.value = startingValue

        print("Creating a new Adder: ", self.value)
account = Adder(3)
print(account)