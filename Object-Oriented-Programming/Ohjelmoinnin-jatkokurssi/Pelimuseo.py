

class Tietokonepeli:
    def __init__(self, nimi: str, julkaisija: str, vuosi: int):
        self.nimi = nimi
        self.julkaisija = julkaisija
        self.vuosi = vuosi


class Pelivarasto:
    def __init__(self):
        # Yksityisiä näkyvyysmääreitä (__) käytetään, kun halutaan, että käyttäjä ei vahingossa (ainakaan helposti)
        # muuta attribuuttien/metodien arvoja ulkoisen koodin toimesta.
        self.__pelit = []

    # Huomaa, että peli-parametri on luokan Tietokonepeli olio.
    def lisaa_peli(self, peli: Tietokonepeli):
        self.__pelit.append(peli)

    def anna_pelit(self):
        return self.__pelit


# Luokka Pelimuseo perii luokan Pelivarasto.
# Alaluokka perii yliluokan attribuutit ja metodit, mutta tämän lisäksi ne voidaan uudelleentoteuttaa alaluokassa.
# Uudelleentoteutetaan metodi anna_pelit() siten, että metodi palauttaa listasta ainoastaan ne pelit,
# jotka on tehty ennen vuotta 1990.

class Pelimuseo(Pelivarasto):

    def __init__(self):
        super().__init__()  # Peritään yliluokan (parent class) attribuutit ja metodit.

    def anna_pelit(self):
        # Kutsutaan yliluokan metodia anna_pelit() super() -funktion avulla,
        # jolloin kaikki pelit tallennetaan pelit-muuttujaan.
        pelit = super().anna_pelit()

        # Luodaan lista, johon tallennetaan silmukan avulla ne pelit, jotka on tehty ennen vuotta 1990.
        g = []
        for game in pelit:
            if game.vuosi < 1990:
                g.append(game)
        return g


if __name__ == "__main__":

    museo = Pelimuseo()
    museo.lisaa_peli(Tietokonepeli("Pacman", "Namco", 1980))
    museo.lisaa_peli(Tietokonepeli("GTA 2", "Rockstar", 1999))
    museo.lisaa_peli(Tietokonepeli("Bubble Bobble", "Taito", 1986))
    for p in museo.anna_pelit():
        print(p.nimi)
