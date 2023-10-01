

# Mikäli listakoosteessa tarvitaan filteröintiä (ehdollisuutta), niin yleinen syntaksi on seuraava:
#   [<lauseke> for <alkio> in <sarja> if <ehtolauseke>]

# Erotuksena listakoosteen perusmuotoon (ilman ehtolausetta) on siis ainoastaan se,
# että listakoosteen loppuun lisätään ehtolause. Alla vielä kertauksena listakooste ilman ehtolauseketta:
#   [<lauseke> for <alkio> in <sarja>]

def poista_pienemmat(luvut: list, raja: int):
    """
    Funktio muodostaa uuden listan, josta on jätetty pois kynnysarvoa pienemmät luvut.

    Args:
        luvut: lista kokonaislukuja.
        raja: kynnysarvo, jota pienemmät luvut jätetään pois uudesta listasta.

    Returns:
        Funktio palauttaa listan, joka sisältää kokonaislukuja.
    """
    return [i for i in luvut if i > raja]


lukuja = [1, 65, 32, -6, 9, 11]
print(poista_pienemmat(lukuja, 10))
print(poista_pienemmat([-4, 7, 8, -100], 0))
