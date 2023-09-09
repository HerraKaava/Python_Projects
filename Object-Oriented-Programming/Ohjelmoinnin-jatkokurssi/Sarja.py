

class Sarja:
    # Konstruktorissa määriteltyjä attribuutteja voidaan käyttää globaalisti metodien sisällä.
    def __init__(self, nimi: str, kausien_lkm: int, genret: list):
        self.nimi = nimi
        self.kausien_lkm = kausien_lkm
        self.genret = genret
        self.arvostelut = []


    def __str__(self):
        # Metodin palautuksen sisältö riippuu siitä, onko arvosteluja annettu vai ei.
        # Tämän takia täytyy tarkistaa, onko arvostelut-listassa alkioita (eli onko sen pituus > 0).
        if len(self.arvostelut) > 0:
            return f"{self.nimi} ({self.kausien_lkm} esityskautta)\n"\
                   f"genret: {', '.join(self.genret)}\n"\
                   f"arvosteluja {len(self.arvostelut)}, keskiarvo {round(sum(self.arvostelut)/len(self.arvostelut), 1)} pistettä"
        else:
            return f"{self.nimi} ({self.kausien_lkm} esityskautta)\n" \
                   f"genret: {', '.join(self.genret)}\n" \
                   "ei arvosteluja"


    def arvostele(self, arvosana: int):
        # 'arvostelut'-lista määriteltiin konstruktorissa, joten sitä voidaan käyttää täällä.
        # Täällä tapahtuu ainoastaan arvostelujen lisäys listaan.
        # Varsinaiset laskut (arvostelujen lkm ja keskiarvo) tapahtuu __str__ -metodissa.
        self.arvostelut.append(arvosana)


def arvosana_vahintaan(arvosana: float, sarjat: list):
    """
    Funktio palauttaa listan sarjoista, joiden arvostelut täyttävät annetun arvosanan vähimmäisvaatimuksen.

    Args:
        arvosana (float): Vähimmäisarvosana, jota etsitään sarjoista.
        sarjat (list): Lista sarjoista, joiden arvosteluja tarkastellaan.

    Returns:
        list: Lista sarjoista, joiden arvostelut täyttävät vähimmäisarvosanan vaatimuksen.
    """
    sarja_lista = []
    for sarja in sarjat:
        for arvostelu in sarja.arvostelut:
            if arvostelu >= arvosana:
                sarja_lista.append(sarja)
    return sarja_lista


def sisaltaa_genren(genre: str, sarjat: list):
    """
    Funktio palauttaa listan sarjoista, jotka sisältävät annetun genren.

    Args:
        genre (str): Genre, jota etsitään sarjoista.
        sarjat (list): Lista sarjoista, joista etsitään genreen liittyviä sarjoja.

    Returns:
        list: Lista sarjoista, jotka sisältävät annetun genren.

    Esimerkki:
        Jos annetaan sisaltaa_genren("Draama", sarjat), funktio palauttaa kaikki sarjat, jotka sisältävät
        "Draama" genren.
    """
    genre_lista = []
    for sarja in sarjat:
        for g in sarja.genret:
            if g == genre:
                genre_lista.append(sarja)
    return genre_lista


if __name__ == "__main__":

    s1 = Sarja("Dexter", 8, ["Crime", "Drama", "Mystery", "Thriller"])
    s1.arvostele(5)

    s2 = Sarja("South Park", 24, ["Animation", "Comedy"])
    s2.arvostele(3)

    s3 = Sarja("Friends", 10, ["Romance", "Comedy"])
    s3.arvostele(2)

    Sarjat = [s1, s2, s3]

    print("arvosana vähintään 4.5:")
    for series in arvosana_vahintaan(4.5, Sarjat):
        print(series.nimi)

    print()    # Tyhjä line konsolin tulostukseen

    print("genre Comedy:")
    for s in sisaltaa_genren("Comedy", Sarjat):
        print(s.nimi)


