from dier_cls import dier
class persoon:
    info = "dit is een klasse persoon"
    def __init__(self,naam,leeftijd,interesses:list):
        self.naam = naam
        self.leeftijd = leeftijd
        if isinstance(interesses,list):
            self.interesses = interesses
        else:
            self.interesses = [interesses]
        self.aantal_interesses = len(self.interesses)
        self.dieren = []

    def print_interesses(self):
        for x in self.interesses:
            print(x)
    def voeg_interesse_toe(self,interesse):
        self.interesses.append(interesse)
    def voeg_dier_toe(self,dier):
        self.dieren.append(dier)
    def toon_dier(self):
        if len(self.dieren)>0:
            for x in self.dieren:
                print(x)
        else:
            print("geen dieren in de lijst")

