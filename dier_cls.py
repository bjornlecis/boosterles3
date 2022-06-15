class dier:
    def __init__(self,naam,soort):
       self.naam = naam
       self.soort = soort
    def __str__(self):
        return "naam {} soort {}".format(self.naam,self.soort)
