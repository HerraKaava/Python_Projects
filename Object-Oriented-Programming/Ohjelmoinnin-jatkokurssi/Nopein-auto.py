

class Auto:
    # Konstruktori
    def __init__(self, merkki: str, huippunopeus: int):
        self.merkki = merkki
        self.huippunopeus = huippunopeus

    def __str__(self):
        return f"Auto (merkki: {self.merkki}, huippunopeus: {self.huippunopeus})"


def nopein_auto(autot: list):
    """
    This function finds the car brand with the highest top speed.

    Args:
        autot (list): List of objects of class Auto.

    Returns:
        str: The brand of the fastest car from the list.
    """
    nopeudet = []
    for auto in autot:
        # Lisätään 'nopeudet'-listaan auton merkki ja nopeus tuplena
        nopeudet.append((auto.merkki, auto.huippunopeus))

    # lambda-funktion avulla määritetään, että max-funktion sisällä vertailu tehdään \
    # indeksin 1 kohdalla olevien arvojen perusteella (joka on auton nopeus).
    # Koska halutaan palauttaa pelkkä auton merkki eikä koko tuplea,
    # indeksoidaan tuplesta 1. elementti.
    return max(nopeudet, key=lambda x: x[1])[0]


if __name__ == "__main__":

    auto1 = Auto("Mersu", 195)
    auto2 = Auto("Lada", 110)
    auto3 = Auto("Ferrari", 280)
    auto4 = Auto("Trabant", 85)

    cars = [auto1, auto2, auto3, auto4]
    print(nopein_auto(cars))    # Ferrari





