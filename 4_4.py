import random

oikea = random.randint(1, 10)

while True:
    try:
        arvaus = int(input("Arvaa luku väliltä 1..10: "))
    except ValueError:
        print("Anna kokonaisluku!")
        continue

    if arvaus < oikea:
        print("Liian pieni arvaus")
    elif arvaus > oikea:
        print("Liian suuri arvaus")
    else:
        print("Oikein!")
        break
