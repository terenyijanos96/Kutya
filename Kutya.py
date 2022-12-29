import random


class Kutya:

    def __init__(self, nev, nem, faj, marmagassag, suly):
        self.nev = nev
        self.nem = nem
        self.faj = faj
        self.marmagassag = marmagassag
        self.suly = suly

    def __str__(self):
        return f"Kutya neve: {self.nev},\nneme: {self.nem},\nfajtája: {self.faj},\nmarmagassága (cm): {self.marmagassag},\n" \
               f"súlya (kg): {self.suly}"

    def tevekenyseg(self):
        veletlen = int(random.random() * 3)
        tevekenysegek_lista = ["ugat", "alszik", "játszik"]
        print(f"{self.nev} éppen {tevekenysegek_lista[veletlen]}.",end="")
        if tevekenysegek_lista[veletlen] == "ugat":
            self.harap()
        else:
            print()

    def harap(self):
        print(f" Vigyázz!! Harapni fog!!")

