

class Kirja:
    # Konstruktori
    def __init__(self, nimi, kirjoittaja, genre, kirjoitusvuosi):
        self.nimi = nimi
        self.kirjoittaja = kirjoittaja
        self.genre = genre
        self.kirjoitusvuosi = kirjoitusvuosi


def vanhempi_kirja(kirja1, kirja2):
    """
    Vertailee kahden kirjan kirjoitusvuosia ja tulostaa tiedon siitä, kumpi kirjoista on vanhempi.

    Args:
        kirja1: Ensimmäinen kirja, jota verrataan kirjoitusvuoden perusteella.
        kirja2: Toinen kirja, jota verrataan kirjoitusvuoden perusteella.

    Returns:
        None

    Prints:
        Funktio tulostaa vanhemman kirjan nimen ja kirjoitusvuoden merkkijonona.
    """
    if kirja1.kirjoitusvuosi < kirja2.kirjoitusvuosi:
        print(f"{kirja1.nimi} on vanhempi, se kirjoitettiin vuonna {kirja1.kirjoitusvuosi}.")

    elif kirja1.kirjoitusvuosi == kirja2.kirjoitusvuosi:
        print(f"{kirja1.nimi} ja {kirja2.nimi} ovat yhtä vanhoja. Ne kirjoitettiin vuonna {kirja1.kirjoitusvuosi}")

    else:
        print(f"{kirja2.nimi} on vanhempi, se kirjoitettiin vuonna {kirja2.kirjoitusvuosi}.")


if __name__ == "__main__":

    python = Kirja("Fluent Python", "Luciano Ramalho", "ohjelmointi", 2015)
    everest = Kirja("Huipulta huipulle", "Carina Räihä", "elämänkerta", 2010)
    norma = Kirja("Norma", "Sofi Oksanen", "rikos", 2015)

    vanhempi_kirja(python, everest)
    vanhempi_kirja(python, norma)

