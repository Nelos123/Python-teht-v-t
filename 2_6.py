import random

kolmelukua = ""
for i range(3):
    numero = random.randint(1, 9)
    kolmelukua += str(numero)

neljalukua = ""
for i range(4):
    numero = random.randint(1, 9)
    neljalukua += str(numero)

print(kolmelukua)
print(neljalukua)