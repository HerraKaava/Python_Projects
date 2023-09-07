
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


def tuotteita_yhteensa(lista):
    # Luodaan tyhjä lista, johon lisätään tuotteiden määrät.
    n = []
    # Luodaan silmukka, joka käy kaikki tuotteet läpi
    for i in range(1, lista.tuotteita()+1):
        # Lisätään iterointivuorossa olevan tuotteen määrä listaan n
        n.append(lista.maara(i))
    # Palautetaan tuotteiden summa (eli määrä).
    return sum(n)


if __name__ == "__main__":
    lista = Kauppalista()
    lista.lisaa("banaanit", 10)
    lista.lisaa("omenat", 5)
    lista.lisaa("ananas", 1)

    print(tuotteita_yhteensa(lista))
