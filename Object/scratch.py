class MyClass:
    def __init__(self, pre):
        self.prefix = pre
        print("Creating a new MyClass", pre)

    def echo(self, words):
        print(self.prefix, words)
    def echoTwice(self, words):
        print(self.prefix, words)
        print(self.prefix, words)
t = MyClass("echo:")
MyClass.echo(t, "apple")


s = MyClass("y")
s.echoTwice("pear")