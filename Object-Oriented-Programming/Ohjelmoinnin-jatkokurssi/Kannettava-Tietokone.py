

class Tietokone:
    # Konstruktori
    def __init__(self, malli: str, nopeus: int):
        self.__malli = malli
        self.__nopeus = nopeus

    # Havainnointimetodi yksityiselle attribuutille malli
    @property
    def malli(self):
        return self.__malli

    # Havainnointimetodi yksityiselle attribuutille nopeus
    @property
    def nopeus(self):
        return self.__nopeus


# Luokka KannettavaTietokone perii luokan Tietokone, jolloin Tietokone on yliluokka ja KannettavaTietokone aliluokka.
# Aliluokalla on käytössä kaikki yliluokan attribuutit ja metodit (elleivät ne ole yksityisiä).
# (Huomaa, että havainnointimetodien avulla attribuutteja voi kuitenkin tarkastella aliluokissa,
# vaikka ne olisivat yksityisiä yliluokassa).
# Perintä tapahtuu kirjoittamalla luokan nimen perään perittävän luokan nimi sulkuihin

# Yliluokan konstruktoriin (tai yliluokkaan muutenkin) viitataan funktion super() avulla.
# Aliluokan konstruktoriin tulee samat parametrit kuin yliluokan (mikäli haluat viitata niihin).
# Lisäksi samat yliluokan parametrit annetaan toisen kerran super()-funktion kutsun jälkeen __init__ -konstruktoriin.
# Huomaa, että aliluokan konstruktoriin voidaan määrittää myös aliluokan omia attribuutteja,
# joita ei esiinny yliluokassa.

class KannettavaTietokone(Tietokone):
    # Konstruktori
    def __init__(self, malli: str, nopeus: int, paino: int):
        super().__init__(malli, nopeus)
        self.paino = paino

    def __str__(self):
        return f"{self.malli}, {self.nopeus} MHz, {self.paino} kg"


if __name__ == "__main__":
    ipm = KannettavaTietokone("IPM MikroMauri", 1500, 2)
    print(ipm)
    print(ipm.nopeus)
    