

class SuperSankari:
    def __init__(self, nimi: str, supervoimat: str):
        self.nimi = nimi
        self.supervoimat = supervoimat

    def __str__(self):
        return f"{self.nimi}, superkyvyt: {self.supervoimat}"


class SuperRyhma:
    def __init__(self, nimi: str, kotipaikka: str):
        self._nimi = nimi
        self._kotipaikka = kotipaikka
        self._jasenet = []

    # Havainnointimetodi suojatulle attribuutille nimi
    @property
    def nimi(self):
        return self._nimi

    # Havainnointimetodi suojatulle attribuutille kotipaikka
    @property
    def kotipaikka(self):
        return self._kotipaikka

    # Huomaa, että sankari-parametri on luokan SuperSankari olio.
    def lisaa_jasen(self, sankari: SuperSankari):
        self._jasenet.append(sankari)

    def tulosta_ryhma(self):
        print(f"{self._nimi}, {self._kotipaikka}")
        print("Jäsenet:")
        for hero in self._jasenet:
            print(hero)
            # Huomaa SuperSankari luokan __str__ -metodi, jonka takia riittää tulostaa tässä jokainen
            # listan 'jasenet' alkio.
            # Luokan SuperSankari __str__ -metodi siis saa aikaan sen,
            # että jokaisen olion nimi ja supervoima tulostetaan.


if __name__ == "__main__":
    
    supermiekkonen = SuperSankari("Supermiekkonen", "Supernopeus, supervoimakkuus")
    nakymaton = SuperSankari("Näkymätön Makkonen", "Näkymättömyys")
    ryhma_z = SuperRyhma("Ryhmä Z", "Kälviä")

    ryhma_z.lisaa_jasen(supermiekkonen)
    ryhma_z.lisaa_jasen(nakymaton)
    ryhma_z.tulosta_ryhma()
