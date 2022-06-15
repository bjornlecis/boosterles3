class Dier2:
    def __init__(self,naam,leeftijd):
        self.naam=naam
        self.leeftijd = leeftijd
    def toon_info_dier(self):
        return "{} {}".format(self.naam,self.leeftijd)


class kat(Dier2):
    def __init__(self,naam,leeftijd,ras):
        super().__init__(naam,leeftijd)
        self.ras = ras
    def toon_info_kat(self):
        return "{} {}".format(super().toon_info_dier(),self.ras)

class hond(Dier2):
    def __init__(self,naam,leeftijd,ras):
        super().__init__(naam,leeftijd)
        self.ras = ras
    def toon_info_hond(self):
        return "{} {}".format(super().toon_info_dier(),self.ras)



k = kat("Garlfied",12,"Luie kat")
h = hond("Bobby",10,"Poedel")
h2 = hond("Samson",10,"Bobtail")
print(k.toon_info_kat())
print(h.toon_info_hond())
if(isinstance(h,Dier2)):
    print("hond")

lijst_dieren = [k,h,h2]
for x in lijst_dieren:
    if isinstance(x,kat):
        print(x.toon_info_dier())
