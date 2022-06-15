from School_classes import *
studenten = []
leerkrachten = []

s1 = leerling("Bart",15,"Genk","Wetenschappen")
s2 = leerling("Sofie",16,"Hasselt","Latijn")
s3 = leerling("Leen",14,"Genk","Wetenschappen")
s4 = leerling("Mark",16,"Bilzen","Wetenschappen")
s5 = leerling("Anneleen",15,"Genk","Economie")

l1 = leerkracht("Inge",42,"Hasselt")
l2 = leerkracht("Frank",38,"Genk")
l3 = leerkracht("Sonja",28,"Genk")

l1.voeg_vak_toe("Frans")
l1.voeg_vak_toe("Latijn")
l2.voeg_vak_toe("Wisunde")
l2.voeg_vak_toe("Biologie")
l3.voeg_vak_toe("Nederlands")
l3.voeg_vak_toe("Engels")
l3.voeg_vak_toe("Geschiedenis")

leerkrachten.extend([l1,l2,l3])
studenten.extend([s1,s2,s3,s4,s5])
