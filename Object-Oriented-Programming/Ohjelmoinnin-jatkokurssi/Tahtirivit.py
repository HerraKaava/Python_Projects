

def tahtirivit(luvut: list):
    """
    Funktio luo uuden tähtirivejä (***) sisältävän listan,
    joiden pituudet vastaavat parametrina annetun listan lukuja.
    Esimerkiksi jos parametrina annettu lista olisi [1, 2, 3],
    uusi lista olisi [*, **, ***].

    Args:
          luvut: lista kokonaislukuja

    Returns:
        Funktio palauttaa uuden listan, joka sisältää tähtirivejä,
        joiden pituudet vastaavat alkuperäisen listan lukuja.
    """
    return [luku * "*" for luku in luvut]


rivit = tahtirivit([1, 2, 3, 4])
for rivi in rivit:
    print(rivi)
