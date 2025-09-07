def main():
    luvut = []

    while True:
        syote = input("Anna luku (tyhjä lopettaa): ")
        if syote == "":
            break
        try:
            luku = int(syote)
            luvut.append(luku)
        except ValueError:
            print("Anna vain kokonaislukuja.")

    luvut.sort(reverse=True)

    print("Viisi suurinta lukua:")
    for luku in luvut[:5]:
        print(luku)


if __name__ == "__main__":
    main()
