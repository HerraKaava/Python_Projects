

class Kauppalista:
    def __init__(self):
        self.tuotteet = []

    def tuotteita(self):
        return len(self.tuotteet)

    def lisaa(self, tuote: str, maara: int):
        self.tuotteet.append((tuote, maara))

    def __iter__(self):
        self.n = 0
        return self

    def __next__(self):
        if self.n < len(self.tuotteet):
            tuote = self.tuotteet[self.n]
            self.n += 1
            return tuote
        else:
            raise StopIteration


def kauppalistan_tuotteet(kauppalista: Kauppalista, maara: int):
    """
    Args:
        kauppalista: Kauppalista-olio.
        maara: tuotteiden määrä.

    Returns:
        Funktio palauttaa Kauppalista-olion ostoksista niiden tuotteiden nimet,
        joita on listalla vähintään parametrin "maara" verran.
    """
    # Kauppalista-olio on tuple (tuote, maara), joten sitä voi indeksoida.
    return [tuote[0] for tuote in kauppalista if tuote[1] >= maara]


if __name__ == "__main__":

    lista = Kauppalista()
    lista.lisaa("banaanit", 10)
    lista.lisaa("omenat", 5)
    lista.lisaa("alkoholiton olut", 24)
    lista.lisaa("ananas", 1)

    print("Tuotteet, joita kauppalistalla on vähintään 8 kappaletta, ovat:")
    for i in kauppalistan_tuotteet(lista, 8):
        print(i)
