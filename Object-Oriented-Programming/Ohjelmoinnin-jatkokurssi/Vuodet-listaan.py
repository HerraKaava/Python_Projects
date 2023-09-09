

from datetime import date

def vuodet_listaan(paivamaarat: list):
    """
    Funktio järjestää sille syötetyn listan, joka sisältää datetime-olioita,
    päivämäärien vuodet suuruusjärjestykseen pienimmästä suurimpaan.

    Args:
        paivamaarat (list): Funktiolle syötettävä lista, joka sisältää datetime-tyyppisiä olioita.

    Returns:
       Funktio palauttaa uuden listan, jossa on päivämäärien vuodet
       suuruusjärjestyksessä pienimmästä suurimpaan.
    """
    # Lista, johon tallennetaan päivämäärien vuodet
    vuodet = []

    for pvm in paivamaarat:
        vuodet.append(pvm.year)

    # 'sorted' -funktio järjestää listan alkiot suuruusjärjestykseen pienimmästä suurimpaan (default).
    # Mikäli alkiot halutaan järjestää suurimmasta pienimpään,
    # tämä onnistuu 'sorted' -funktion argumentilla 'reverse=True'.
    return sorted(vuodet)


if __name__ == "__main__":

    paiva1 = date(2019, 2, 3)
    paiva2 = date(2006, 10, 10)
    paiva3 = date(1993, 5, 9)

    vuodet = vuodet_listaan([paiva1, paiva2, paiva3])
    for v in vuodet:
        print(v)
        