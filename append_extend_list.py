import data_les
import math
lijst_a = [5,3,6,9]
lijst_a.append(7)
lijst_b = [9,6,2,5]
print(lijst_a)
lijst_a.extend([2])
print(lijst_a)
lijst_a.extend(lijst_b)
print(lijst_a)
for x in lijst_a:
    print(x,end=" ")
print()
aantal = lijst_a.count(5)
print(aantal)

dict = {"Naam":"Bjorn","Leeftijd":31}
print(dict.items())
print(data_les.lijst)
print(data_les.dubbel(5))

pi = math.pi
