from School_classes import *
from School_data import leerkrachten,studenten

def toon_alle_studenten():
    for x in studenten:
        print(x)
def wijzig_studierichting(naam_leerling,nieuwe_studierichting):
    for x in studenten:
        if x.naam == naam_leerling:
            x.studierichting = nieuwe_studierichting
def wijzig_woonplaats(naam,nieuwe_woonplaats):
    personen = []
    personen.extend(studenten)
    personen.extend(leerkrachten)
    for x in personen:
        if naam == x.naam:
            x.wijzig_woonplaats(nieuwe_woonplaats)
def voeg_student_toe(naam,leeftijd,woonplaats,studierichtig):
    studenten.append(leerling(naam,leeftijd,woonplaats,studierichtig))

def sorteer_studenten_op_naam():
    studenten.sort(key=lambda x:x.naam)
    toon_alle_studenten()
def zoek_op_woonplaats(woonplaats):
    filter = []
    for x in studenten:
        if x.woonplaats == woonplaats:
            filter.append(x.naam)
    print(filter)

def ken_vak_toe_aan_leerkracht(leerkracht,vak):
    for x in leerkrachten:
        if leerkracht == x.naam:
            x.voeg_vak_toe(vak)




