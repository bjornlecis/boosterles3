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

    def print_interesses(self):
        for x in self.interesses:
            print(x)
    def voeg_interesse_toe(self,interesse):
        self.interesses.append(interesse)
