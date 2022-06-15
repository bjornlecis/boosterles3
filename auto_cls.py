class auto:
    def __init__(self,merk,model):
        self.merk = merk
        self.model = model
        self.snelheid = 0

    def __str__(self):
        return "merk {} model {}".format(self.merk,self.model)

    def toon_info(self):
        print("merk:{} model {} rijdt aan {} kmph".format(self.merk,self.model,self.snelheid))
    def versnel(self):
        self.snelheid += 20

    def vertraag(self):
        if self.snelheid >= 20:
            self.snelheid -= 20
    def geef_snelheid(self):
        return self.snelheid




