

def suodata_kielletyt(merkkijono: str, kielletyt: str):
    """
    Funktio muodostaa annetusta merkkijonosta uuden version,
    joka ei sisällä kiellettyjä merkkejä.

    Args:
        merkkijono: merkkijono, josta muodostetaan uusi sana.
        kielletyt: merkkijono, joka sisältää kielletyt merkit.

    Returns:
        Funktio palauttaa parametrina annetusta merkkijonosta uuden version,
        joka ei sisällä kiellettyjä merkkejä (toinen parametri).
    """
    # [<lauseke> for <alkio> in <sarja> if <ehtolauseke>]
    return "".join([char for char in merkkijono if char not in kielletyt])

    # Yllä listakooste kerää ensiksi kirjaimet merkkijonosta, jotka ovat sallittuja.
    # Tämän jälkeen join() -metodilla liitetään listan sanat yhdeksi merkkijonoksi.


if __name__ == "__main__":
    lause = "Suo! kuokka, ja python: hieno yhdistelmä!??!?!"
    suodatettu = suodata_kielletyt(lause, "!?:,.")
    print(suodatettu)


