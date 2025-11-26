class Julkaisu:
    def __init__(self, nimi):
        self.nimi = nimi

    def tulosta(self):
        print(f"\n--- {self.nimi} ---")
        self.tulosta_tiedot()


class Kirja(Julkaisu):
    def __init__(self, nimi, kirjoittaja, sivumaara):
        super().__init__(nimi)
        self.kirjoittaja = kirjoittaja
        self.sivumaara = sivumaara

    def tulosta_tiedot(self):
        print(f"Kirjoittaja: {self.kirjoittaja}")
        print(f"Sivumäärä: {self.sivumaara}")


class Lehti(Julkaisu):
    def __init__(self, nimi, paatoimittaja):
        super().__init__(nimi)
        self.paatoimittaja = paatoimittaja

    def tulosta_tiedot(self):
        print(f"Päätoimittaja: {self.paatoimittaja}")


aku_ankka = Lehti("Aku Ankka", "Aki Hyyppä")
hytti6 = Kirja("Hytti n:o 6", "Rosa Liksom", 200)

aku_ankka.tulosta()
hytti6.tulosta()
