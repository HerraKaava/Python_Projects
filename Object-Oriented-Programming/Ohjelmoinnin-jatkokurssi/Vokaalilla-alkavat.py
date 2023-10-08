

def vokaalilla_alkavat(sanat: list):
    """
    Funktio saa parametrikseen merkkijonoja sisältävän listan ja muodostaan uuden listan,
    joka sisältää ainoastaan alkuperäisen listan ne sanat, jotka alkavat vokaalilla (a, e, i, o, u, y, ä, ö).

    Args:
        sanat: lista, joka sisältää merkkijonoja.

    Returns:
        Funktio palauttaa listan, joka sisältää ainoastaan vokaalilla alkavia sanoja.
    """
    return [i for i in sanat if i[0].lower() in "aeiouyäö"]


klista = ["auto", "mopo", "Etana", "kissa", "Koira", "OMENA", "appelsiini"]
for vok in vokaalilla_alkavat(klista):
    print(vok)
