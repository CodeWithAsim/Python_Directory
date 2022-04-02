class Humans:
    def __init__(self, n, o):
        self.name = n
        self.occupation = o

    def works(self):
        if self.occupation == "actor":
            print(self.name, "performs acting")
        elif self.occupation == "player":
            print(self.name, "plays games")

    def speaks(self):
        print("Hi, I am ", self.name)


babar = Humans("Babar", "player")
babar.works()
babar.speaks()

print("---------------------------")

anushka = Humans("Anushka", "actor")
anushka.works()
anushka.speaks()
