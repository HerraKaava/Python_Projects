

# Tässä tehtävässä toteutetaan luokka Paivays, jonka avulla on mahdollista käsitellä päivämääriä.
# Oletetaan tässä tehtävässä yksinkertaisuuden vuoksi, että jokaisessa kuussa on 30 päivää.

class Paivays:
    # Konstruktori
    def __init__(self, paiva: int, kuukausi: int, vuosi: int):
        self.paiva = paiva
        self.kuukausi = kuukausi
        self.vuosi = vuosi


    # Toteutetaan päivämäärien vertailuoperaattorit <, >, ==, !=

    # <
    def __lt__(self, other):
        if self.vuosi < other.vuosi:
            return True
        elif (self.vuosi == other.vuosi) and (self.kuukausi < other.kuukausi):
            return True
        elif (self.vuosi == other.vuosi) and (self.kuukausi == other.kuukausi) and (self.paiva < other.paiva):
            return True
        else:
            return False


    # >
    def __gt__(self, other):
        if self.vuosi > other.vuosi:
            return True
        elif (self.vuosi == other.vuosi) and (self.kuukausi > other.kuukausi):
            return True
        elif (self.vuosi == other.vuosi) and (self.kuukausi == other.kuukausi) and (self.paiva > other.paiva):
            return True
        else:
            return False


    # ==
    def __eq__(self, other):
        if (self.vuosi == other.vuosi) and (self.kuukausi == other.kuukausi) and (self.paiva == other.paiva):
            return True
        else:
            return False


    # !=
    def __ne__(self, other):
        # Huomaa, että toista metodia voidaan kutsua toisen sisällä.
        # Täällä tarkistetaan, pitääkö yhtäsuuruus paikkansa.
        # The "not" operator is used to negate the result, so it returns "True",
        # if the objects are not equal and "False" if they are equal.
        return not self.__eq__(other)


    def __str__(self):
        return f"{self.paiva}.{self.kuukausi}.{self.vuosi}"


    # Operaattori luo uuden päivämäärän, joka on lisättävän lukeman päiviä verran suurempi ku alkuperäne pvm.
    # Alkuperäinen päivämäärä ei saa muuttua.
    def __add__(self, other):
        day = self.paiva + other
        month = self.kuukausi
        year = self.vuosi

        # Jos päivä > 30 (tässä tehtävässä kuukaudessa aina 30 päivää),
        # niin kasvatetaan kuukauden arvoa yhdellä ja vähennetään päivästä 30 päivää (kuukauden verran).
        # Tätä toistetaan niin kauan, kunnes päivä <= 30.
        while day > 30:
            month += 1
            day -= 30

        # Tässä sama logiikka kuukausien ja vuosien osalta kuin yllä.
        while month > 12:
            year += 1
            month -= 12

        return Paivays(day, month, year)


    # Tämä metodi palauttaa päivämäärien eron PÄIVISSÄ laskettuna.
    # Koska oletetaan, että jokaisessa kuukaudessa on 30 päivää,
    # niin vuosien päivien lukumäärä on 12*30=360.
    def __sub__(self, other):
        total1 = self.paiva + self.kuukausi * 30 + self.vuosi * 360
        total2 = other.paiva + other.kuukausi * 30 + other.vuosi * 360
        return abs(total1 - total2)


if __name__ == "__main__":
    
    p1 = Paivays(4, 10, 2020)
    p2 = Paivays(2, 11, 2020)
    p3 = Paivays(28, 12, 1985)

    print(p2 - p1)
    print(p1 - p2)
    print(p1 - p3)
    print(p1 < p2)


