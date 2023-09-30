

# List comprehensionin (listakoosteen) syntaksi on perusmuodossaan:
#   [<lauseke> for <alkio> in <sarja>]

import numpy as np

def neliojuuret(luvut: list):
    """
    Funktio luo uuden listan parametrina annetun listan alkioiden neliöjuurista.

    Args:
        luvut: lista, joka sisältää lukuja (int tai float).

    Returns:
        Funktio palauttaa uuden listan, jossa on alkuperäisen listan alkioiden neliöjuuret.
    """
    return [np.sqrt(luku) for luku in luvut]


print(neliojuuret([1, 2, 3, 4]))
