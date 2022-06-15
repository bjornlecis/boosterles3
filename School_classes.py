class persoon:
    def __init__(self,naam,leeftijd,woonplaats):
        self.naam = naam
        self.leeftijd = leeftijd
        self.woonplaats = woonplaats
    def __str__(self):
        return "{} {} {}".format(self.naam,self.woonplaats,self.leeftijd)
    def wijzig_woonplaats(self,woonplaats):
        self.woonplaats = woonplaats


class leerling(persoon):
    def __init__(self,naam,leeftijd,woonplaats,studierichting):
        super().__init__(naam,leeftijd,woonplaats)
        self.studierichting = studierichting
    def __str__(self):
        return "{} studierichting {}".format(super().__str__(),self.studierichting)

class leerkracht(persoon):
    def __init__(self,naam,leeftijd,woonplaats):
        super().__init__(naam,leeftijd,woonplaats)
        self.vakken = []
    def __str__(self):
        return "{} studierichting {}".format(super().__str__())
    def toon_vakken(self):
        if self.vakken > 0:
            for x in self.vakken:
                print(x)
        else:
            print("leerkracht heeft nog geen vak")
    def voeg_vak_toe(self,vak):
        self.vakken.append(vak)
