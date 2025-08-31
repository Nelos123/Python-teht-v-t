luvut = []

while True:
    syote = input("Anna luku (tyhjä lopettaa): ")
    if syote == "":
        break
    try:
        luvut.append(int(syote))
    except ValueError:
        print("Syöte ei kelpaa, yritä uudelleen.")

luvut.sort(reverse=True)

print("\nViisi suurinta lukua:")
for luku in luvut[:5]:
    print(luku)
