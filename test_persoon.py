from persoon_prog_cls import persoon
from operator import attrgetter

p = persoon("Peter",50,["Vogelspotten","x","y"])
p2 = persoon("Ben",20,["z","Drinken"])
p3 = persoon("Mark",20,"x")
p4 = persoon("Dennis",35,"x")
p5 = persoon("Eric",45,"x")

lijst_personen = [p,p2,p3,p4,p5]

for x in lijst_personen:
    print(x.naam)

lijst_personen.sort(key=attrgetter('naam'))
print("sorteer")
for x in lijst_personen:
    print(x.naam)
