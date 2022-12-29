from Kutya import *

mano = Kutya("Manó", "szuka", "puli", 38, 9)
hogolyo = Kutya("Hógolyó", "kan", "puli", 44, 15)
toto = Kutya("Totó", "szuka", "pumi", 42, 13)

kutyak = [mano, hogolyo, toto]

for k in kutyak:
    k.tevekenyseg()
