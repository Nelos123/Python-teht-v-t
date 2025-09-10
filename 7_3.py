def lentoasemat():
    lentoasemat = {}

    while True:
        print("\nValitse toiminto:")
        print("1 = Lisää uusi lentoasema")
        print("2 = Hae lentoasema")
        print("3 = Lopeta")
        valinta = input("Valinta: ")

        if valinta == "1":
            icao = input("Anna lentoaseman ICAO-koodi: ").upper()
            nimi = input("Anna lentoaseman nimi: ")
            lentoasemat[icao] = nimi
            print("Lentoasema tallennettu!")

        elif valinta == "2":
            icao = input("Anna ICAO-koodi: ").upper()
            if icao in lentoasemat:
                print(f"Lentoaseman nimi: {lentoasemat[icao]}")
            else:
                print("Lentoasemaa ei löydy.")

        elif valinta == "3":
            print("Ohjelma lopetetaan.")
            break
        else:
            print("Virheellinen valinta.")


if __name__ == "__main__":
    lentoasemat()