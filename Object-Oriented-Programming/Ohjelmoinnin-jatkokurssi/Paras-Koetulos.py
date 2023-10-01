

class Koesuoritus:
    def __init__(self, nimi: str, arvosana1: int, arvosana2: int, arvosana3: int):
        self.nimi = nimi
        self.arvosana1 = arvosana1
        self.arvosana2 = arvosana2
        self.arvosana3 = arvosana3

    def __str__(self):
        return (f"Nimi:{self.nimi}, arvosana1: {self.arvosana1}" +
                f", arvosana2: {self.arvosana2}, arvosana3: {self.arvosana3}")


def parhaat_tulokset(suoritukset: list):
    """
    Funktio kertoo kunkin henkilön parhaan suorituksen.

    Args:
        suoritukset: lista Koesuoritus-olioita.

    Returns:
        Funktio palauttaa listakoostetta (list comprehension) käyttäen uuden listan,
        johon on tallennettu jokaisen suorituksen paras arvosana
    """
    return [max(koe.arvosana1, koe.arvosana2, koe.arvosana3) for koe in suoritukset]


if __name__ == "__main__":
    
    jokke = Koesuoritus("Jokke", 11, 5, 3)
    mikko = Koesuoritus("Mikko", 16, 10, 5)
    lasse = Koesuoritus("Lasse", 27, 20, 15)
    l = [jokke, mikko, lasse]
    print(parhaat_tulokset(l))
