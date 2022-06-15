from tolk_data import tolken
from tolk_cls import tolk

def toon_tolk():
    for x in tolken:
        print(x)

def voeg_tolk_toe(naam,geslacht):
    tolken.append(tolk(naam,geslacht))

def toon_talen_tolk(naam):
    for x in tolken:
        if x.naam == naam:
            x.print_talen()
def voeg_taal_toe_aan_tolk(naam, taal):
     for x in tolken:
        if x.naam == naam:
            x.voeg_taal_toe(taal)


voeg_tolk_toe("Mario","M")
toon_tolk()
toon_talen_tolk("Maria")
voeg_taal_toe_aan_tolk("Maria", "Chinees")
toon_talen_tolk("Maria")
