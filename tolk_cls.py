class tolk:
    def __init__(self,naam,geslacht):
        self.naam = naam
        self.geslacht = geslacht
        self.talen = []
    def __str__(self):
        g = str(self.geslacht).upper()
        if g == "V":
            return "Mevrouw {}".format(self.naam)
        else:
            return "Meneer {}".format(self.naam)

    def voeg_taal_toe(self,taal):
       self.talen.append(taal)
       
    def print_talen(self):
        for x in self.talen:
            print(x)
