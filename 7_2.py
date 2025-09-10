def nimet():
    nimet_set = set()
    while True:
        nimi = input("Anna nimi (tyhjä lopettaa): ")
        if nimi == "":
            break
        if nimi not in nimet_set:
            print("Uusi nimi")
            nimet_set.add(nimi)
        else:
            print("Aiemmin syötetty nimi")

    print("\nSyötetyt nimet:")
    for n in nimet_set:
        print(n)


if __name__ == "__main__":
    nimet()