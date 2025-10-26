import random

class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.matka = 0

    def kiihdytä(self, muutos):
        self.nopeus += muutos
        if self.nopeus > self.huippunopeus:
            self.nopeus = self.huippunopeus
        elif self.nopeus < 0:
            self.nopeus = 0

    def kulje(self, tunnit):
        self.matka += self.nopeus * tunnit


# Pääohjelma
autot = []
for i in range(1, 11):
    huippu = random.randint(100, 200)
    tunnus = f"ABC-{i}"
    autot.append(Auto(tunnus, huippu))

# Kilpailu jatkuu kunnes joku saavuttaa vähintään 10000 km
kilpailu_kaynnissa = True
tunti = 0
while kilpailu_kaynnissa:
    tunti += 1
    for auto in autot:
        muutos = random.randint(-10, 15)
        auto.kiihdytä(muutos)
        auto.kulje(1)

        if auto.matka >= 10000:
            kilpailu_kaynnissa = False
            break

print(f"\nKilpailu päättyi {tunti} tunnin jälkeen!\n")

print(f"{'Rekisteri':<10} {'Huippu':<8} {'Nopeus':<8} {'Matka':<10}")
print("-" * 40)
for auto in autot:
    print(f"{auto.rekisteritunnus:<10} {auto.huippunopeus:<8} {auto.nopeus:<8} {auto.matka:<10.1f}")
