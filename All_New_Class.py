class ComicBookCharacters():
    def __init__(self, codename, power, crush):
        self.codename = codename
        self.power = power
        self.crush = crush
    pass


class XMen(ComicBookCharacters):
    def rolecall(self):
        print("I am", self.codename)
        print(self.team, "team")
        print("Mutant and Proud")


    def __init__(self, codename, power, crush, team = "Gold"):
        super().__init__(codename, power, crush)
        self.team = team



scott_summers = XMen("Cyclops", "Optic Blasts", None)
jean_grey = XMen("Marvel Girl", "Telekinesis + Telepathy", None)
hank_mccoy = XMen("Beast", "Super Strength and Agility", jean_grey)
warren_worthington = XMen("Angel", "Flight", None)
bobby_drake = XMen("Iceman", "Cryokinesis", None)
laura_kinney = XMen("Wolverine", "Is a Wolverine", warren_worthington)

jean_grey.crush = hank_mccoy
warren_worthington.crush = laura_kinney

scott_summers.rolecall()