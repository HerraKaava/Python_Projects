

class Koesuoritus:
    # Konstruktori
    def __init__(self, suorittaja: str, pisteet: int):
        self.suorittaja = suorittaja
        self.pisteet = pisteet

    # __str__() is a special method that can be defined within a class to customize \
    # the string representation of objects of that class.
    def __str__(self):
        return f'Koesuoritus (suorittaja: {self.suorittaja}, pisteet: {self.pisteet})'


def hyvaksytyt(suoritukset: list, pisteraja: int):
    """
    Creates a new list from the provided list, containing only approved exam results.

    Args:
         suoritukset: a list of exam results (instances of the Koesuoritus class)
         pisteraja: the minimum accepted score

    Returns:
        The function constructs and returns a new list
        containing only the approved results from the input list.
    """
    approved = []
    for suoritus in suoritukset:
        if suoritus.pisteet >= pisteraja:
            approved.append(suoritus)
    return approved


if __name__ == "__main__":

    s1 = Koesuoritus("Pekka", 12)
    s2 = Koesuoritus("Pirjo", 19)
    s3 = Koesuoritus("Pauli", 15)
    s4 = Koesuoritus("Pirkko", 9)
    s5 = Koesuoritus("Petriina", 17)

    hyv = hyvaksytyt([s1, s2, s3, s4, s5], 15)
    for hyvaksytty in hyv:
        print(hyvaksytty)
