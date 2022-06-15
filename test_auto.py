#van file import klasse naam
from auto_cls import auto
autos = []

a = auto("Ford","Focus")
a.toon_info()
b = auto("Ford","Fiesta")
"""
for i in range(1,5):
    a.versnel()
a.toon_info()
a.vertraag()
a.toon_info()
"""
def voeg_auto_toe():
    merk = input("geef het merk")
    model = input("geef het model")
    a = auto(merk,model)
    autos.append(a)

def merk_in_lijst():
    merk = input("geef het merk in")
    gevonden = False
    for x in autos:
       if x.merk == merk:
            print("merk in lijst")
            gevonden = True
            break
    if gevonden == False:
        print("auto niet gevonden")

def auto_in_lijst(merk,model):
    gevonden = False
    for x in autos:
       if x.merk == merk and x.model == model:
            print("auto in lijst")
            gevonden = True
            break
    if gevonden == False:
        print("auto niet gevonden")

def verwijder_auto(merk):
    for x, o in enumerate(autos):
        if o.merk == merk:
            del autos[x]
            x -= 1



print(type(a))
a.snelheid = 50
print(a.geef_snelheid())
print(auto.geef_snelheid(b))
autos.append(a)
autos.append(b)
#voeg_auto_toe()
autos.append(auto("Audi","a4"))
for x in autos:
    print(x)
#merk_in_lijst()
#auto_in_lijst("Ford","Mondeo")
for x in autos:
    print(x)
verwijder_auto("Ford")
print("Na verwijder")
for x in autos:
    print(x)
