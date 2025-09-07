import random

def heita_noppaa():
    return random.randint(1, 6)

def main():
    silmaluku = 0
    while silmaluku != 6:
        silmaluku = heita_noppaa()
        print("Heitto:", silmaluku)

if __name__ == "__main__":
    main()
