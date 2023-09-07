

class Koesuoritus:
    def __init__(self, suorittaja: str, pisteet: int):
        self.suorittaja = suorittaja
        self.pisteet = pisteet

    # __str__() is a special method that can be defined within a class to customize \
    # the string representation of objects of that class.
    def __str__(self):
        return f'Koesuoritus (suorittaja: {self.suorittaja}, pisteet: {self.pisteet})'


def hyvaksytyt(suoritukset: list, pisteraja: int):
    """
    Muodostetaan uusi lista parametrina annetusta listasta,
    jossa on ainoastaan hyväksytyt koesuoritukset.

    Args:
         suoritukset: lista koesuorituksia (Koesuoritus-luokan olioita)
         pisteraja: alin hyväksytty pistemäärä

    Returns:
        Funktio muodostaa ja palauttaa uuden listan,
        johon on tallennettu ainoastaan hyväksytyt suoritukset listalta.
    """
    hyvaksytyt = []
    for suoritus in suoritukset:
        if suoritus.pisteet >= pisteraja:
            hyvaksytyt.append(suoritus)

    return hyvaksytyt


if __name__ == "__main__":
    s1 = Koesuoritus("Pekka", 12)
    s2 = Koesuoritus("Pirjo", 19)
    s3 = Koesuoritus("Pauli", 15)
    s4 = Koesuoritus("Pirkko", 9)
    s5 = Koesuoritus("Petriina", 17)

    hyv = hyvaksytyt([s1, s2, s3, s4, s5], 15)
    for hyvaksytty in hyv:
        print(hyvaksytty)
