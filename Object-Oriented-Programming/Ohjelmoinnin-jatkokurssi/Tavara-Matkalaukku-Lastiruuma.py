

# Tietojen piilottamista asiakkaalta kutsutaan kapseloinniksi.

class Tavara:
    # Konstruktori.
    # Huomaa, että attribuutit ovat kapseloitu (piilotettu asiakkaalta).
    def __init__(self, nimi: str, paino: int):
        self.__nimi = nimi
        self.__paino = paino


    def __str__(self):
        return f"{self.__nimi} ({self.__paino} kg)"


    # Tämä metodi palauttaa tavaran nimen (joka määritetään konstruktorissa)
    def nimi(self):
        return self.__nimi


    # Tämä metodi palauttaa tavaran painon (joka määritetään konstruktorissa)
    def paino(self):
        return self.__paino


class Matkalaukku:
    # Konstruktori
    def __init__(self, maksimipaino: int):
        self.maksimipaino = maksimipaino
        self.tavarat = []


    # Metodi laskee ja palauttaa tavarat-listassa olevien tavaroiden yhteispainon.
    def tavaroiden_paino(self):
        yhteispaino = 0
        for i in self.tavarat:
            yhteispaino += i.paino()
        return yhteispaino


    # Huomaa, että tavara-parametri on luokan Tavara olio.
    # Tavaroiden yhteispaino ei saa ylittää maksimipainoa.
    # Jos maksimipaino ylittyisi lisättävän tavaran vuoksi,
    # niin metodi ei saa lisätä uutta tavaraa laukkuun.
    # Tarkistetaan siis ehtolausekkeessa seuraava summa:
    # tavarat-listassa olevien tavaroiden yhteispaino + tällä hetkellä lisättävänä olevan tavaran paino.
    def lisaa_tavara(self, tavara: Tavara):
        # tavarat-listassa olevien tavaroiden yhteispaino.
        yhteispaino = self.tavaroiden_paino()

        # Jos yhteispaino + tällä hetkellä lisättävänä olevan tavaran paino on pienempi kuin sallittu maksimipaino,
        # niin lisätään parametrina annettu tavara tavarat-listaan (muussa tapauksessa ei tehdä mitään).
        if yhteispaino + tavara.paino() <= self.maksimipaino:
            self.tavarat.append(tavara)


    def __str__(self):
        # tavarat-listassa olevien tavaroiden yhteispaino.
        yhteispaino = self.tavaroiden_paino()

        # Kielenhuoltoa (monikko vs. yksikkö)
        if len(self.tavarat) == 1:
            return f"{len(self.tavarat)} tavara ({yhteispaino} kg)"
        else:
            return f"{len(self.tavarat)} tavaraa ({yhteispaino} kg)"


    def tulosta_tavarat(self):
        for j in self.tavarat:
            # nimi ja paino -metodit ovat määritelty Tavara-luokassa,
            # mutta koska tavarat-listan alkiot ovat luokan Tavara olioita,
            # niillä on luokan Tavara attribuutit ja metodit.
            print(f"{j.nimi()} ({j.paino()} kg)")


    # Tämä metodi palauttaa matkalaukun yhteispainoa kuvaavan kokonaisluvun,
    # joka on sen sisältävien tavaroiden painojen summa.
    def paino(self):
        # Local variable, joten ei haittaa, vaikka toisella metodilla on myös weight-muuttuja.
        weight = 0
        for i in self.tavarat:
            weight += i.paino()
        return weight


    def raskain_tavara(self):
        # Jos tavarat-lista on tyhjä, palautetaan None.
        if not self.tavarat:
            return None

        # max() -funktio yhdessä lambda-funktion kanssa saa aikaan sen,
        # että tavarat-listasta palautetaan se luokan Tavara olio, jolla on suurin paino.
        # Tämä on TODELLA kätevää!!

        heaviest_object = max(self.tavarat, key=lambda x: x.paino())
        return heaviest_object

        # Huomaa, että koska tavarat-lista sisältää luokan Tavara olioita,
        # jotka ovat sidottu seuraavaan __str__() -metodiin:

        #     def __str__(self):
        #         return f"{self.__nimi} ({self.__paino} kg)"

        # niin return heaviest_object palauttaa automaattisesti tiedon painavimman objektin nimestä ja painosta.


class Lastiruuma:
    # Konstruktori
    def __init__(self, maksimipaino: int):
        self.maksimipaino = maksimipaino
        self.lastiruuma = []


    # Metodi laskee ja palauttaa lastiruuman matkalaukkujen yhteispainon
    def lastiruuman_paino(self):
        total_weight = 0
        for i in self.lastiruuma:
            total_weight += i.paino()
        return total_weight


    # Huomaa, että parametri matkis on luokan Matkalaukku olio.
    def lisaa_matkalaukku(self, matkis: Matkalaukku):
        # Apumuuttuja, joka kirjaa lastiruuman matkalukkujen yhteispainon.
        total_weight = self.lastiruuman_paino()

        # Jos lastiruuman matkalaukkujen yhteispaino + lisättävänä olevan Matkalaukku-olion paino ei ylitä
        # sallittua maksimipainoa, niin matkalaukku voidaan lisätä (muutoin sitä ei tule lisätä).
        if total_weight + matkis.paino() <= self.maksimipaino:
            self.lastiruuma.append(matkis)


    # Tämä metodi palauttaa merkkijonon muotoa "x matkalaukkua, tilaa y kg"
    # (tilaa on jäljellä tietysti maksimipaino miinus lastiruuman paino).
    def __str__(self):
        # Täälläkin tarvitaan lastiruuman paino.
        total_weight = self.lastiruuman_paino()

        # Monikko vs. yksikkö (kielenhuoltoa)
        if len(self.lastiruuma) == 1:
            return f"{len(self.lastiruuma)} matkalaukku, tilaa {self.maksimipaino - total_weight} kg"
        else:
            return f"{len(self.lastiruuma)} matkalaukkua, tilaa {self.maksimipaino - total_weight} kg"


    # Tämä metodi tulostaa kaikki lastiruuman matkalaukuissa olevat tavarat.
    # Koitin tehdä tämän aluksi samalla tavalla kuin luokan Matkalaukku tulosta_tavarat() -metodin:
    #     def tulosta_tavarat(self):
    #         for j in self.tavarat:
    #             print(f"{j.nimi()} ({j.paino()} kg)")

    # Tämä kuitenkin antoi virheen AttributeError: 'Lastiruuma' object has no attribute 'nimi'.
    # Tämä johtuu siitä, että kuten virheviesti sanoo, Lastiruuma-oliolla ei ole olemassa attribuutteja nimi ja paino.
    # However, lastiruuma-lista sisältää matkalaukku-olioita, joilla on metodi tulosta_tavarat(),
    # jossa iteroidaan tavarat-lista, joka sisältää Tavara-olioita, joilla on attribuutit nimi ja paino,
    # ja jotka ovat sidottu seuraavaan __str__ -metodiin:
    #
    #        def __str__(self):
    #            return f"{self.__nimi} ({self.__paino} kg)"
    #
    # joka siis palauttaa nimen ja painon muodossa "Nimi (x kg)"

    def tulosta_tavarat(self):
        for matkis in self.lastiruuma:
            matkis.tulosta_tavarat()


if __name__ == "__main__":

    kirja = Tavara("Aapiskukko", 2)
    puhelin = Tavara("Nokia 3210", 1)
    tiiliskivi = Tavara("Tiiliskivi", 4)

    matkalaukku = Matkalaukku(10)
    matkalaukku.lisaa_tavara(kirja)
    matkalaukku.lisaa_tavara(puhelin)
    matkalaukku.lisaa_tavara(tiiliskivi)

    raskain = matkalaukku.raskain_tavara()
    print(f"Raskain tavara: {raskain}")