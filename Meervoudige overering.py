class vader:
    def __init__(self,voornaam,achternaam,geboortejaar):
        self.voornaam = voornaam
        self.achternaam = achternaam
        self.geboortejaar = geboortejaar
    def toon_info_vader(self):
        return "{} {} geboortejaar {}".format(self.voornaam,self.achternaam,self.geboortejaar)

class moeder:
    def __init__(self,voornaam,achternaam,geboortejaar):
        self.voornaam = voornaam
        self.achternaam = achternaam
        self.geboortejaar = geboortejaar
    def toon_info_moeder(self):
        return "{} {} geboortejaar {}".format(self.voornaam,self.achternaam,self.geboortejaar)


class kind():
    def __init__(self,vader,moeder,voornaam,achternaam,geboortejaar):
        self.vader = vader
        self.moeder = moeder
        self.voornaam = voornaam
        self.achternaam = achternaam
        self.geboortejaar = geboortejaar

    def toon_info_kind(self):
        return "{} {} geboortejaar {}\n{}\n{}".format(self.voornaam,self.achternaam,self.geboortejaar,self.moeder.toon_info_moeder(),self.vader.toon_info_vader())


v = vader("Bart","Bertjens",1975)
m = moeder("An","Jansen",1977)
k = kind(v,m,"Jefke","Bertjens",2000)
print(k.toon_info_kind())
print(k.moeder.toon_info_moeder())


