

class Alkio:
    """ Luokka mallintaa yhtä alkiota binääripuussa """
    def __init__(self, arvo, vasen_lapsi: 'Alkio' = None, oikea_lapsi: 'Alkio' = None):
        self.arvo = arvo
        self.vasen_lapsi = vasen_lapsi
        self.oikea_lapsi = oikea_lapsi


def suurin_alkio(juuri: Alkio):
    """
    Funktio etsii binääripuun suurimman alkion.

    Args:
        juuri: luokan Alkio olio, joka mallintaa yhtä alkiota binääripuussa.

    Returns:
        Funktio palauttaa binääripuun suurimman alkion.
    """
    # Alustetaan juurialkion arvo suurimmaksi alkioksi
    # (binääripuun juurialkio on sen ylin alkio, jonka "jälkeläisiä" kaikki muut alkiot ovat).
    suurin = juuri.arvo

    # Tarkistetaan, onko joku vasemman haaran jälkeläisen arvo suurempi kuin juurialkio.
    if juuri.vasen_lapsi is not None:
        suurin_alkio(juuri.vasen_lapsi)     # Visualisoi tätä rekursiota debuggerin avulla
        suurin = max(suurin, suurin_alkio(juuri.vasen_lapsi))

    # Toistetaan sama tarkastelu oikean haaran jälkeläisille.
    if juuri.oikea_lapsi is not None:
        suurin_alkio(juuri.oikea_lapsi)
        suurin = max(suurin, suurin_alkio(juuri.oikea_lapsi))

    # Palautetaan suurin alkio
    return suurin


if __name__ == "__main__":

    puu = Alkio(2)

    puu.vasen_lapsi = Alkio(3)
    puu.vasen_lapsi.vasen_lapsi = Alkio(5)
    puu.vasen_lapsi.oikea_lapsi = Alkio(8)

    puu.oikea_lapsi = Alkio(4)
    puu.oikea_lapsi.oikea_lapsi = Alkio(11)

    print(suurin_alkio(puu))
