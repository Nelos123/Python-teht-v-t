import mysql.connector

def hae_lentokentta(icao):
    yhteys = mysql.connector.connect(
        host='localhost',
        user='root',
        password='salasana',
        database='flight_game'
    )
    cursor = yhteys.cursor()
    sql = "SELECT name, municipality FROM airport WHERE ident = %s"
    cursor.execute(sql, (icao,))
    tulos = cursor.fetchone()
    cursor.close()
    yhteys.close()
    return tulos

icao = input("Anna lentoaseman ICAO-koodi: ")
kentta = hae_lentokentta(icao)

if kentta:
    print(f"Lentokenttä: {kentta[0]}, sijaintikunta: {kentta[1]}")
else:
    print("Lentokenttää ei löytynyt.")
