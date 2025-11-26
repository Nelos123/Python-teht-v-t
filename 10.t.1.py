class Hissi:
    def __init__(self, alinkerros, ylinkerros):
        self.alinkerros = alinkerros
        self.ylinkerros = ylinkerros
        self.nykyinenkerros = alinkerros

    def kerros_ylös(self):
        if self.nykyinenkerros < self.ylinkerros:
            self.nykyinenkerros += 1
            print(f"Hissi on nyt kerroksessa {self.nykyinenkerros}")

    def kerros_alas(self):
        if self.nykyinenkerros > self.alinkerros:
            self.nykyinenkerros -= 1
            print(f"Hissi on nyt kerroksessa {self.nykyinenkerros}")

    def siirry_kerrokseen(self, kerros):
        while self.nykyinenkerros < kerros:
            self.kerros_ylös()
        while self.nykyinenkerros > kerros:
            self.kerros_alas()


if __name__ == "__main__":
    h = Hissi(1, 10)
    print(f"Hissi on aluksi kerroksessa {h.nykyinenkerros}")

    haluttu_kerros = int(input("Mihin kerrokseen haluat mennä? "))
    h.siirry_kerrokseen(haluttu_kerros)

    print("Takaisin alimpaan kerrokseen.")
    h.siirry_kerrokseen(h.alinkerros)
