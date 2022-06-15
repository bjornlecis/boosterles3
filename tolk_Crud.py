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
def voeg_taal_toe_aan_tolk(naam):
     for x in tolken:
        if x.naam == naam:
            taal = input("geef de taal in")
            x.voeg_taal_toe(taal)

def toon_tolk_taal(taal):
    tolk_taal = []
    for x in tolken:
        for y in x.talen:
            if taal == y:
                tolk_taal.append(x.naam)
    print(tolk_taal)


def toon_alle_talen():
    talen = []
    for x in tolken:
        for y in x.talen:
            talen.append(y)
    set_talen = set(talen)
    print(set_talen)



voeg_tolk_toe("Mario","M")
toon_tolk()
toon_talen_tolk("Maria")
voeg_taal_toe_aan_tolk("Maria", "Chinees")
toon_talen_tolk("Maria")
toon_tolk_taal("Frans")
tolken.sort(key=lambda x:x.naam)
toon_tolk()
voeg_taal_toe_aan_tolk("Mario","Nederlands")
toon_alle_talen()
