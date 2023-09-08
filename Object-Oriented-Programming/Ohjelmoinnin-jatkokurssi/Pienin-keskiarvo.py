

def pienin_keskiarvo(henkilo1, henkilo2, henkilo3):
    """
    Laskee kolmen sanakirjan arvojen keskiarvot ja palauttaa sen sanakirjan,
    jonka arvojen keskiarvo on pienin.

    Args:
        henkilo1 (dict): Ensimmäinen sanakirja, josta lasketaan keskiarvo.
        henkilo2 (dict): Toinen sanakirja, josta lasketaan keskiarvo.
        henkilo3 (dict): Kolmas sanakirja, josta lasketaan keskiarvo.

    Returns:
        dict: Sanakirja, jonka arvojen keskiarvo on pienin.

    Note:
        - Jokaisen syötteen odotetaan olevan sanakirja, joka sisältää arvoja.
        - Tyhjiä sanakirjoja ei käsitellä erityisesti.
    """
    # Tallennetaan funktiolle syötetyt parametrit listaan silmukkaa varten
    params = [henkilo1, henkilo2, henkilo3]

    # Luodaan tyhjä sanakirja, jonka avulla voidaan palauttaa se sanakirja, jonka arvojen keskiarvo on pienin.
    sanakirja_pienin_ka = {}

    # Luodaan apumuuttuja, johon keskiarvoja verrataan.
    # Alustetaan apumuuttujan arvo riittävän suureksi.
    pienin = float("inf")

    # Luodaan tyhjä lista keskiarvojen laskemista varten.
    l = []

    for d in params:
        # sanakirjoilla on values-metodi, joka palauttaa ainoastaan sanakirjan arvot.
        for val in d.values():
            # Koska sanakirjojen 1. arvo ei ole luku, täytyy määritellä erikseen,
            # että listaan l lisätään ainoastaan luvut (muuten tulee error summaa laskettaessa).
            if (type(val) == int) or (type(val) == float):
                l.append(val)

        # Lasketaan keskiarvo
        keskiarvo = sum(l) / len(l)

        # Jos keskiarvo on pienempi kuin pienin-muuttujan arvo, niin päivitetään se.
        if keskiarvo < pienin:
            pienin = keskiarvo
            # Päivitetään palautettava sanakirja
            sanakirja_pienin_ka = d

        # "Tyhjennetään" lista uuden keskiarvon laskemista varten.
        l = []

    return sanakirja_pienin_ka


if __name__ == "__main__":

    h1 = {"nimi": "Keijo", "tulos1": 2, "tulos2": 3, "tulos3": 3}
    h2 = {"nimi": "Reijo", "tulos1": 5, "tulos2": 1, "tulos3": 8}
    h3 = {"nimi": "Veijo", "tulos1": 3.01, "tulos2": 0.94, "tulos3": 1}
    print(pienin_keskiarvo(h1, h2, h3))
