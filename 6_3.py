def on_alkuluku(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def main():
    luku = int(input("Anna kokonaisluku: "))
    if on_alkuluku(luku):
        print(f"Luku {luku} on alkuluku.")
    else:
        print(f"Luku {luku} ei ole alkuluku.")

if __name__ == "__main__":
    main()
