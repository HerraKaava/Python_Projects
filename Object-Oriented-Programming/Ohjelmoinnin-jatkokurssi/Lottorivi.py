

# Listakoosteessa (list comprehension) voi käyttää ehtolauseen ohella myös vaihtoehtoista haaraa (else):
#   [<lauseke1> if <ehto> else <lauseke2> for <alkio> in <sarja>]

class Lottorivi:
    # Konstruktori
    def __init__(self, kierroksen_nro: int, oikeat_nrot: list[int]):
        self.kierroksen_nro = kierroksen_nro
        self.oikeat_nrot = oikeat_nrot


    # Metodi palauttaa kokonaislukuna tiedon siitä, kuinka monta osumaa pelatussa rivissä oli.
    # Oikea rivi on siis konstruktorissa määritelty lista, joka sisältää 7 kokonaislukua.
    def osumien_maara(self, pelattu_rivi: list):
        # Listakoosteessa verrataan jokaista pelatun rivin alkiota oikeaan riviin.
        # Mikäli pelatun rivin alkio on oikeassa rivissä, se lisätään uuteen palautettavaan listaan.
        # Huomaa, että listakooste on len() -funktion sisällä,
        # koska halutaan nimenomaan tieto siitä, kuinka monta osumaa tuli.
        # Jos len() -funktio otettaisiin pois, metodi palauttaisi listan,
        # joka sisältää ne numerot, jotka menivät oikein.
        return len([i for i in pelattu_rivi if i in self.oikeat_nrot])


    def osumat_paikoillaan(self, pelattu_rivi: list):
        # Metodi palauttaa uuden listan siten, että mikäli pelatussa rivissä on osuma,
        # se lisätään sellaisenaan uuteen listaan.
        # Jos taas pelatussa rivissä on huti (väärä numero), tämän paikalle laitetaan luku -1.
        return [num if num in self.oikeat_nrot else -1 for num in pelattu_rivi]


if __name__ == "__main__":

    oikea = Lottorivi(8, [1, 2, 3, 10, 20, 30, 33])
    oma_rivi = [1, 4, 7, 10, 11, 20, 30]
    print(oikea.osumien_maara(oma_rivi))
    print(oikea.osumat_paikoillaan(oma_rivi))
