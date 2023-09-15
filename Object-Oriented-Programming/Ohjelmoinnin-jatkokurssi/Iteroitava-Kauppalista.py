

class Kauppalista:
    def __init__(self):
        self.tuotteet = []

    def tuotteita(self):
        return len(self.tuotteet)

    def lisaa(self, tuote: str, maara: int):
        self.tuotteet.append((tuote, maara))

    def tuote(self, n: int):
        return self.tuotteet[n - 1][0]

    def maara(self, n: int):
        return self.tuotteet[n - 1][1]


    # Iteraattorin alustusmetodi
    # Tässä tulee alustaa iteroinnissa käytettävä(t) muuttuja(t)
    def __iter__(self):
        self.n = 0

        # Metodi palauttaa viittauksen olioon itseensä, koska iteraattori on toteutettu samassa luokassa
        return self

    # Metodi palauttaa seuraavan alkion (jos ei ole enempää alkioita, heitetään tapahtuma StopIteration)
    def __next__(self):
        if self.n < len(self.tuotteet):

            # Poimitaan listasta nykyinen alkio (indeksillä n)
            x = self.tuotteet[self.n]

            # Kasvatetaan laskuria yhdellä
            self.n += 1

            # Palautetaan tuote.
            # Huomaa, että tuote-lista sisältää tupleja --> x on siis tuple, jonka sisältö on (tuote, määrä).
            return x

        else:
            raise StopIteration


if __name__ == "__main__":

    lista = Kauppalista()
    lista.lisaa("banaanit", 10)
    lista.lisaa("omenat", 5)
    lista.lisaa("ananas", 1)

    for product in lista:
        print(f"{product[0]}: {product[1]} kpl")
