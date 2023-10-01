

def pituudet(listat: list):
    """
    Funktio kertoo parametrina annettujen listojen pituudet.

    Args:
        listat: listoista koostuva lista (nested list).

    Returns:
        Funktio palauttaa uuden listan, joka sisältää parametrina annetun listan listojen pituudet.
    """
    return [len(lista) for lista in listat]


nums = [[1, 2, 3, 4, 5], [324, -1, 31, 7], []]
print(pituudet(nums))
