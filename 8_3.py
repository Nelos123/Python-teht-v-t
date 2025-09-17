import mysql.connector
from geopy.distance import geodesic

def hae_koordinaatit(icao):
    yhteys = mysql.connector.connect(
        host='localhost',
        user='root',
        password='salasana',
        database='flight_game'
    )
    cursor = yhteys.cursor()
    sql = "SELECT latitude_deg, longitude_deg FROM airport WHERE ident = %s"
    cursor.execute(sql, (icao,))
    tulos = cursor.fetchone()
    cursor.close()
    yhteys.close()
    return tulos

icao1 = input("Anna ensimmäinen ICAO-koodi: ")
icao2 = input("Anna toinen ICAO-koodi: ")

koord1 = hae_koordinaatit(icao1)
koord2 = hae_koordinaatit(icao2)

if koord1 and koord2:
    etaisyys = geodesic(koord1, koord2).kilometers
    print(f"Lentokenttien {icao1} ja {icao2} välinen etäisyys on {etaisyys:.2f} km")
else:
    print("Toisen lentokentän koordinaatteja ei löytynyt.")
