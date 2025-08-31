import random

pisteidenMäärä = int(input("Anna pisteidenmäärä: "))
kierros = 0
while kierros < pisteidenMäärä:
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)

    print(f"Pisteen sijainti on {x}. {y} ")
    paikka = x**2 + y**2
    if paikka < 1 and paikka == 1 :
       print(f"Piste on ympyrän sisällä")