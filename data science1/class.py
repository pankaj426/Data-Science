class Human:
    def __init__(self, n, o):
        self.name = n
        self.occupation = o

    def do_work(self):
        if self.occupation == "tennis player":
            print(self.name,"play tennis")
        elif self.occupation == "actor":
            print(self.name, "shoots a filem")
    def speaks(self):
        print(self.name, "sya how are you")

tom = Human("tom cruise", "actor")
tom.do_work()
tom.speaks()


