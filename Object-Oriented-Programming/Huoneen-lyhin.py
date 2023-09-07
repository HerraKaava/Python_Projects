

class Henkilo:
    # Konstruktori
    def __init__(self, nimi: str, pituus: int):
        self.nimi = nimi
        self.pituus = pituus

    def __str__(self):
        return self.nimi


class Huone:
    # Konstruktori
    def __init__(self):
        self.henkilot = []


    def lisaa(self, henkilo: Henkilo):
        # Metodi lisää henkilot-listaan parametrina annetun luokan Henkilo olion
        self.henkilot.append(henkilo)


    def on_tyhja(self):
        # "if not" tarkistaa, onko lista tyhjä.
        # If the list is empty, the statement evaluates to True --> enter the block and return None.
        if not self.henkilot:
            return True
        else:
            return False


    def tulosta_tiedot(self):
        # Luodaan tyhjä lista, johon tallennetaan henkilot-listan henkilöiden pituudet alla olevan silmukan avulla.
        yhteispituus = []
        for henkilo in self.henkilot:
            yhteispituus.append(henkilo.pituus)
        print(f"Huoneessa on {len(self.henkilot)} henkilöä, yhteispituus {sum(yhteispituus)}")

        # Luodaan vielä toinen silmukka, jossa tulostetaan henkilot-listan kunkin henkilön nimi ja pituus.
        for henkilo in self.henkilot:
            print(f"{henkilo.nimi} ({henkilo.pituus} cm)")


    def lyhin(self):
        # Jos henkilot-lista on tyhjä, palautetaan None.
        if not self.henkilot:
            return None
        else:
            # Muussa tapauksessa palautetaan lyhin henkilö.
            # Huomaa, että tämä palauttaa lyhimmän henkilön nimen, jonka tyyppi on <class '__main__.Henkilo'>
            lyhin_hlo = min(self.henkilot, key=lambda x: x.pituus)
            return lyhin_hlo


    def poista_lyhin(self):
        # Jos henkilot-lista on tyhjä, palautetaan None.
        if not self.henkilot:
            return None

        # Huomaa, että saman luokan sisällä määritettyjä metodeja voidaan kutsua muiden metodien sisällä.
        # Tässä kutsutaan lyhin() metodia (eli tallennetaan viittaus lyhimmästä henkilöstä lyhin_hlo -muuttujaan).
        lyhin_hlo = self.lyhin()

        # Tallennetaan indeksi -muuttujaan lyhimmän henkilön indeksi listassa.
        indeksi = self.henkilot.index(lyhin_hlo)
        
        # Nyt, kun lyhimmän henkilön indeksi tiedetään, se voidaan poistaa listasta pop() -metodilla.
        # Huomaa, että pop() -metodi palauttaa listasta poistettavan alkion ja muokkaa listaa inplace.
        # 'return self.henkilot.pop(indeksi)' siis poistaa lyhimmän henkilön listasta ja palauttaa tuon henkilön nimen.
        return self.henkilot.pop(indeksi)


if __name__ == "__main__":
    huone = Huone()

    print("Huone tyhjä?", huone.on_tyhja())
    print("Lyhin:", huone.lyhin())

    huone.lisaa(Henkilo("Lea", 183))
    huone.lisaa(Henkilo("Kenya", 182))
    huone.lisaa(Henkilo("Nina", 172))
    huone.lisaa(Henkilo("Auli", 186))

    print()

    print("Huone tyhjä?", huone.on_tyhja())
    print("Lyhin:", huone.lyhin())

    print()

    huone.tulosta_tiedot()