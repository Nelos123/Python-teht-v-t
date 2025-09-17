import mysql.connector

def hae_kenttien_tyypit(maakoodi):
    yhteys = mysql.connector.connect(
        host='localhost',
        user='root',
        password='salasana',
        database='flight_game'
    )
    cursor = yhteys.cursor()
    sql = """
        SELECT type, COUNT(*) 
        FROM airport 
        WHERE iso_country = %s 
        GROUP BY type
    """
    cursor.execute(sql, (maakoodi,))
    tulokset = cursor.fetchall()
    cursor.close()
    yhteys.close()
    return tulokset

maakoodi = input("Anna maakoodi (esim. FI): ")
tyypit = hae_kenttien_tyypit(maakoodi)

print(f"Lentokenttien lukumäärät maassa {maakoodi}:")
for tyyppi, maara in tyypit:
    print(f"{tyyppi}: {maara}")
