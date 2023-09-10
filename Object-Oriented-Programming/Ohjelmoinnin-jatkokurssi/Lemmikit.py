

class Lemmikki:
    # Konstruktori
    def __init__(self, nimi: str, kuvaus: str):
        self.nimi = nimi
        self.kuvaus = kuvaus

    def __str__(self):
        return f"{self.nimi} ({self.kuvaus})"


# Huomaa, että Henkilo-luokan sisällä käytetään konstruktorissa parametrina Lemmikki-luokkaa.
class Henkilo:
    # Konstruktori
    def __init__(self, nimi: str, lemmikki: Lemmikki):
        self.nimi = nimi
        self.lemmikki = lemmikki

    def __str__(self):
        return f"{self.nimi}, kaverina {self.lemmikki.nimi}, joka on {self.lemmikki.kuvaus}"
        # Huomaa, että koska 'lemmikki'-attribuutti on luokan 'Lemmikki' olio, sillä on 'kuvaus'-attribuutti


if __name__ == "__main__":
    
    x = Henkilo("Arto", Lemmikki("Musti", "pieni koira"))
    print(x)