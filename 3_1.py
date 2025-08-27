pituus = int(input("Anna kuhan pituus (cm): "))

alaraja = 37

if pituus < alaraja:
    puuttuu = alaraja - pituus
    print(f"Kuha on alamittainen. Laske kuha takaisin järveen! Pituudesta puuttuu {puuttuu} cm.")
else:
    print("Kuha on sallitun mittainen. Voit ottaa sen saaliiksi.")
