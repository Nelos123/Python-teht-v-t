import random

arpakuutiot = int(input("Anna arpakuutioiden määrä: "))
heitot = []
for i in range(1, arpakuutiot + 1):
    silmaluku = random.randint(1, 6)
    print(f"Arpakuutio {i}: {silmaluku}")
    heitot.append(silmaluku)

print(f"\nHeittojen summa: {sum(heitot)}")
print(f"Suurin heitto: {max(heitot)}")
print(f"Pienin heitto: {min(heitot)}")
