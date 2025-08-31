kayttaja = int(input("Anna luku: "))
alkuluku = True

if kayttaja < 2:
    alkuluku = False
else:

    for nuppi in range(2, kayttaja):
        if kayttaja % nuppi == 0:
            alkuluku = False
            break

if alkuluku:
    print(f"{kayttaja} on alkuluku.")
else:
    print(f"{kayttaja} ei ole alkuluku.")
