class Hissi:
    def __init__(self, alin, ylin):
        self.alin = alin
        self.ylin = ylin
        self.nykyinen = alin

    def siirry_kerrokseen(self, kerros):
        if kerros < self.alin or kerros > self.ylin:
            print(f"Virhe: kerros {kerros} ei ole välillä {self.alin}-{self.ylin}.")
            return

        while self.nykyinen != kerros:
            self.nykyinen += 1 if self.nykyinen < kerros else -1
            print(f"Hissi on nyt kerroksessa {self.nykyinen}")


class Talo:
    def __init__(self, alin, ylin, hissien_maara):
        self.alin = alin
        self.ylin = ylin
        self.hissit = [Hissi(alin, ylin) for _ in range(hissien_maara)]

    def aja_hissia(self, hissin_numero, kerros):
        if not (1 <= hissin_numero <= len(self.hissit)):
            print("Virhe: hissin numero ei kelpaa.")
            return

        print(f"\nAjetaan hissiä {hissin_numero} kerrokseen {kerros}:")
        self.hissit[hissin_numero - 1].siirry_kerrokseen(kerros)


# Testi
talo = Talo(1, 10, 3)
talo.aja_hissia(1, 5)
talo.aja_hissia(2, 8)
talo.aja_hissia(1, 1)
