class Hissi:
    def __init__(self, alin, ylin):
        self.alin, self.ylin, self.nykyinen = alin, ylin, alin

    def siirry_kerrokseen(self, kerros):
        while self.nykyinen != kerros:
            self.nykyinen += 1 if self.nykyinen < kerros else -1
            print(f"Hissi on nyt kerroksessa {self.nykyinen}")


class Talo:
    def __init__(self, alin, ylin, hissien_maara):
        self.hissit = [Hissi(alin, ylin) for _ in range(hissien_maara)]

    def aja_hissia(self, hissin_numero, kerros):
        if 1 <= hissin_numero <= len(self.hissit):
            print(f"\nAjetaan hissiä {hissin_numero} kerrokseen {kerros}:")
            self.hissit[hissin_numero - 1].siirry_kerrokseen(kerros)
        else:
            print("Virheellinen hissin numero.")

    def palohalytys(self):
        print("\n*** PALO HÄLYTYS! ***")
        print("Kaikki hissit siirretään pohjakerrokseen.\n")
        for i, hissi in enumerate(self.hissit, start=1):
            print(f"Hissi {i}:")
            if hissi.nykyinen == hissi.alin:
                print(f"Hissi on jo pohjakerroksessa ({hissi.alin}).")
            else:
                hissi.siirry_kerrokseen(hissi.alin)


# Testaus
talo = Talo(1, 10, 3)
talo.aja_hissia(1, 5)
talo.aja_hissia(2, 8)
talo.aja_hissia(1, 1)
talo.palohalytys()
