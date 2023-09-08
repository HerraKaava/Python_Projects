

class Lemmikki:

    # Konstruktori
    def __init__(self, nimi, laji, syntymavuosi):
        self.nimi = nimi
        self.laji = laji
        self.syntymavuosi = syntymavuosi


def uusi_lemmikki(nimi, laji, syntymavuosi):
    """
    Luo ja palauttaa uuden Lemmikki-olion annetulla nimellä, lajilla ja syntymävuodella.

    Args:
        nimi (str): Lemmikin nimi.
        laji (str): Lemmikin laji.
        syntymavuosi (int): Lemmikin syntymävuosi.

    Returns:
        Lemmikki: Uusi Lemmikki-olio, joka sisältää annetut tiedot.
    """
    # Luokkia voidaan käyttää esimerkiksi funktioiden parametreina tai paluuarvoina.
    # Tässä luokkaa Lemmikki käytetään funktion paluuarvona.
    return Lemmikki(nimi, laji, syntymavuosi)


if __name__ == "__main__":
    musti = uusi_lemmikki("Musti", "koira", 2017)
    print(musti.nimi)
    print(musti.laji)
    print(musti.syntymavuosi)
