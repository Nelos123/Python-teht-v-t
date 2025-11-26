import requests

API_KEY = "d7277e3d9993344e24fccf29613b5e38"   # lisää oma OpenWeather API key
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def hae_saa(paikkakunta: str):
    params = {
        "q": paikkakunta,
        "appid": API_KEY,   # hae lämpötila Kelvineinä
        "lang": "fi"        # sääkuvaus suomeksi, jos mahdollista
    }

    vastaus = requests.get(BASE_URL, params=params)
    vastaus.raise_for_status()

    data = vastaus.json()

    kuvaus = data["weather"][0]["description"]
    lampotila_kelvin = data["main"]["temp"]
    lampotila_celsius = lampotila_kelvin - 273.15   # muunnos °C:ksi

    return kuvaus, lampotila_celsius

def main():
    paikkakunta = input("Anna paikkakunnan nimi: ")

    try:
        kuvaus, lampotila = hae_saa(paikkakunta)
        print(f"Sää paikkakunnalla {paikkakunta}: {kuvaus}")
        print(f"Lämpötila: {lampotila:.1f} °C")
    except requests.HTTPError:
        print("Virhe haettaessa säätietoja. Tarkista paikkakunta ja API key.")

if __name__ == "__main__":
    main()
