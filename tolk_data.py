from tolk_cls import tolk
tolken = []

a = tolk("Maria","V")
b = tolk("Marco","M")
c = tolk("Fatima","V")
d = tolk("Jean","M")
e = tolk("Jane","V")
a.voeg_taal_toe("Frans")
a.voeg_taal_toe("Engels")
a.voeg_taal_toe("Spaans")
b.voeg_taal_toe("Engels")
b.voeg_taal_toe("Italiaans")
c.voeg_taal_toe("Arabisch")
d.voeg_taal_toe("Frans")
d.voeg_taal_toe("Duits")
e.voeg_taal_toe("Engels")
e.voeg_taal_toe("Russisch")

tolken.extend([a,b,c,d,e])
