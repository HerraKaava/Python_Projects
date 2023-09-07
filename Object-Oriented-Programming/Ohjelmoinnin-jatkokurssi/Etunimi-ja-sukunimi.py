

class Henkilo:

    # Konstruktori
    def __init__(self, nimi: str):
        self.nimi = nimi

    def anna_etunimi(self):
        # Syötteenä annettava nimi on merkkijono, joten se voidaan hajottaa split() -metodilla.
        # split() -metodi hajottaa merkkijonon esim. välilyöntien kohdalta (kuten tässä).
        # Merkkijonon eri osat tallennetaan listaan, joten ne voidaan indeksoida.
        etunimi = self.nimi.split(" ")[0]
        # Etunimi täytyy palauttaa return-avainsanan avulla, muuten palautetaan "None".
        return etunimi

    def anna_sukunimi(self):
        sukunimi = self.nimi.split(" ")[1]
        return sukunimi

if __name__ == "__main__":
    pekka = Henkilo("Pekka Python")
    print(pekka.anna_etunimi())
    print(pekka.anna_sukunimi())
