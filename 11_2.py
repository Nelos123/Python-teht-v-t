class Auto:
    def __init__(self, rekisteri, huippunopeus):
        self.rekisteri = rekisteri
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.matka = 0

    def kulje(self, tunnit=1):
        self.matka += self.nopeus * tunnit


class Sähköauto(Auto):
    def __init__(self, rekisteri, huippunopeus, akkukapasiteetti):
        super().__init__(rekisteri, huippunopeus)
        self.akkukapasiteetti = akkukapasiteetti


class Polttomoottoriauto(Auto):
    def __init__(self, rekisteri, huippunopeus, bensatankki):
        super().__init__(rekisteri, huippunopeus)
        self.bensatankki = bensatankki


sahko = Sähköauto("ABC-15", 180, 52.5)
poltto = Polttomoottoriauto("ACD-123", 165, 32.3)

sahko.nopeus = 150
poltto.nopeus = 140

for _ in range(3):
    sahko.kulje()
    poltto.kulje()

print(f"{sahko.rekisteri} on ajanut {sahko.matka} km")
print(f"{poltto.rekisteri} on ajanut {poltto.matka} km")
