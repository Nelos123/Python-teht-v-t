leiviskatnauloina = 20
naulatluoteina = 32
luotigrammoina = 13.3

leiviskat = float(input("anna leiviskät: "))
naulat = float(input("anna naulat: "))
luodit = float(input("anna luodit: "))

luodityht = (leiviskatnauloina * naulatluoteina + naulat *  naulatluoteina + luodit)

grammat = luodityht *  luotigrammoina

kg = int(grammat//1000)
jgrammat = grammat % 1000

print("masssa nykymittojen mukaan: ")
print(f"{jgrammat}kg")