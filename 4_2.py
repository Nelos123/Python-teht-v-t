tuuma = float(input("Anna tuumamäärä (negatiivinen lopettaa): "))

while tuuma >= 0:
    senttimetrit = tuuma * 2.54
    print(f"{tuuma} tuumaa = {senttimetrit} cm")
    tuuma = float(input("Anna tuumamäärä (negatiivinen lopettaa): "))

print("Ohjelma lopetettu.")
