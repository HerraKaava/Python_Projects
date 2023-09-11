

# Luokkamuuttujiin viitataan siis luokan nimen avulla, esimerkiksi Kaupunki.postinumerot,
# ja oliomuuttujiin eli attribuutteihin olion nimen avulla
# (oliomuuttujiin voi luonnollisesti viitata vasta, kun luokasta on muodostettu olio).

class Kaupunki:

    # Luokkamuuttuja (ns. staattinen muuttuja).
    # Tätä muuttujaa voidaan käyttää koko luokassa viittaamalla luokan nimeen (Kaupunki).
    postinumerot = {"Helsinki": "00100",
                    "Turku": "20100",
                    "Tampere": "33100",
                    "Jyväskylä": "40100",
                    "Oulu": "90100"
                    }

    # Konstruktori
    def __init__(self, nimi: str, asukasluku: int):
        self.__nimi = nimi
        self.__asukasluku = asukasluku

    # Havainnointimetodi piilotetulle attribuutille nimi
    @property
    def nimi(self):
        return self.__nimi

    # Havainnointimetodi piilotetulle attribuutille asukasluku
    @property
    def asukasluku(self):
        return self.__asukasluku

    def __str__(self):
        return f"{self.__nimi} ({self.__asukasluku} as.)"


# Luokkametodi eli staattinen metodi on luokassa oleva metodi,
# jota ei ole sidottu mihinkään luokasta muodostettuun olioon.
# Niinpä luokkametodia voi kutsua ilman, että luokasta muodostetaan oliota.
print(Kaupunki.postinumerot)
