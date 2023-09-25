

class Raha:
    # Konstruktori
    # Tietojen piilottamista asiakkaalta kutsutaan kapseloinniksi.
    # Kapseloidaan kaikki attribuutit (tehdään niistä yksityisiä).
    def __init__(self, eurot: int, sentit: int):
        self.__eurot = eurot
        self.__sentit = sentit


    def __str__(self):
        # The ":02d" is a formatting specifier used to ensure that each component has a minimum width of 2 digits,
        # and if necessary, leading zeros are added.
        return f"{self.__eurot}.{self.__sentit:02d} eur"


    # Kahden Raha-olion yhtäsuuruuden vertailu.
    def __eq__(self, toinen):
        # Tässä palautetaan True, jos vertailtavien olioiden eurot ja sentit ovat yhtäsuuret,
        # muutoin palautetaan False.
        return (self.__eurot == toinen.__eurot) and (self.__sentit == toinen.__sentit)


    # Toteutetaan samaan tapaan kahdelle Raha-oliolle vertailuoperaattorit: <, >, !=

    # <
    def __lt__(self, toinen):
        summa1 = self.__eurot + self.__sentit
        summa2 = toinen.__eurot + toinen.__sentit
        if summa1 < summa2:
            return True
        else:
            return False

    # >
    def __gt__(self, toinen):
        # Täällä voidaan käyttää __lt__() -metodia.
        # "not" avainsana on negaatio Pythonissa eli jos __lt__() -metodi palauttaa True (eli raha on pienempi),
        # niin täällä palautetaan False.
        # Jos taas __lt__() -metodi palauttaa False (raha on suurempi), niin täällä palautetaan True.
        return not self.__lt__(toinen)

    # !=
    def __ne__(self, toinen):
        # Sama logiikka kuin __qt__() -metodissa.
        return not self.__eq__(toinen)


    # Toteutetaan Raha-olioille yhteen- ja vähennyslaskuoperaatiot.
    # Molempien operaatioiden tulee palauttaa uusi Raha-olio,
    # ja ne eivät saa muuttaa olioa itseään tai parametrina olevaa olioa!
    # Muistutuksena; self-muuttuja luokan sisällä viittaa nykyiseen olioon.
    # Tyypillinen tapa käyttää self-muuttujaa onkin viitata olion omiin piirteisiin
    # (esimerkiksi attribuuttien arvoihin).

    # +
    def __add__(self, toinen):
        eurot = self.__eurot + toinen.__eurot

        # Senteissä täytyy ottaa huomioon, että 100 snt = 1 eur.
        sentit = self.__sentit + toinen.__sentit
        if sentit >= 100:
            eurot += 1
            sentit -= 100
        return Raha(eurot, sentit)

    def __sub__(self, toinen):
        eurot = self.__eurot - toinen.__eurot
        sentit = self.__sentit - toinen.__sentit

        if sentit < 0:
            eurot -= 1
            sentit = 100 - abs(sentit)

        if eurot < 0:
            raise ValueError("negatiivinen tulos ei sallittu")

        return Raha(eurot, sentit)


if __name__ == "__main__":

    e1 = Raha(1, 0)
    e2 = Raha(2, 0)

    e3 = e1 + e2

    print(e1 + e2)      # 3.00 eur
    print(e1 < e2)      # True
    print(e1 > e2)      # False
    print(e1 == e2)     # False
    print(e1 != e2)     # True
