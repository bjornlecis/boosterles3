def splits_getallen(getal:int):
    hulp_getal = getal%1000
    d = (getal-hulp_getal)/1000
    getal = hulp_getal
    hulp_getal = getal%100
    h = (getal-hulp_getal)/100
    getal = hulp_getal
    hulp_getal = getal%10
    t = (getal-hulp_getal)/10
    print("{}D {}H {}T {}E".format(d,h,t,hulp_getal))


splits_getallen(51520)

oppv = lambda b,h:(b*h)/2
print(oppv(5,4))
