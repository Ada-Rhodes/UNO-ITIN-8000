class XMen():
    def __init__(self, codename, power, crush):
        self.codename = codename
        self.power = power
        self.crush = crush
    pass


scott_summers = XMen("Cyclops", "Optic Blasts", None)
jean_grey = XMen("Marvel Girl", "Telekinesis + Telepathy", None)
hank_mccoy = XMen("Beast", "Super Strength and Agility", jean_grey)
warren_worthington = XMen("Angel", "Flight", None)
bobby_drake = XMen("Iceman", "Cryokinesis", None)
laura_kinney = XMen("Wolverine", "Is a Wolverine", warren_worthington)

jean_grey.crush = hank_mccoy
warren_worthington.crush = laura_kinney

print(laura_kinney.power)