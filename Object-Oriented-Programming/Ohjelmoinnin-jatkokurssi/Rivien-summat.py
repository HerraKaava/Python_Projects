

def rivien_summat(matriisi):
    """
    Funktio lisää jokaiselle matriisin riville uuden alkion (sarakkeen), jonka arvo on rivin alkioiden summa.

    Args:
        matriisi (list): Funktiolle syötettävä matriisi.

    Returns:
       Funktio ei palauta mitään, vaan muokkaa parametrinaan saamaansa matriisia.
    """
    for row in matriisi:
        # append-metodi lisää alkion listan loppuun, eli matriisien näkökulmasta se luo uuden sarakkeen.
        row.append(sum(row))


M = [[1, 2, 2], [3, 4, 2]]
rivien_summat(M)
print(M)
