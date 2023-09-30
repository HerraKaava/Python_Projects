

# Sanakirjakoosteen (dict comprehension) yleinen syntaksi:
#   {<avainlauseke>: <arvolauseke> for <alkio> in <sarja>}

def pituudet(merkkijonot: list):
    """
    Funktio luo sanakirjan, jossa avaimina on listan merkkijonot ja arvoina merkkijonojen pituudet.

    Args:
         merkkijonot: lista merkkijonoja.

    Returns:
        Funktio palauttaa sanakirjan, joka luotiin yllä määritellyllä tavalla.
    """
    return {merkkijono: len(merkkijono) for merkkijono in merkkijonot}


if __name__ == "__main__":

    sanalista = ["suo", "kuokka", "python", "ja", "koodari"]
    sanojen_pituudet = pituudet(sanalista)
    print(sanojen_pituudet)
    
