


def sulut_tasapainossa(merkkijono: str):
    """
    Funktio tarkistaa, onko sen parametrina olevassa merkkijonossa sulut tasapainossa
    eli onko jokaista "aukeavaa" sulkumerkkiä kohti oma "sulkeutuva" sulkumerkki
    ja että kaari- ja hakasulkeet eivät mene ristiin.
    Funktio jättää huomiotta kaikki muut merkit kuin sulkumerkit.
    """
    # Otetaan ihan aluksi merkkijonosta talteen ainoastaan kaari- ja hakasulkeet,
    # sillä muut kuin sulkumerkit tulee jättää huomioitta.
    # Tämä toiminnallisuus voidaan toteuttaa näppärästi listakoosteen avulla.
    sulkumerkit = [char for char in merkkijono if char in "()[]"]

    # Jos sulkumerkit -listan pituus on 0, niin tällöin varmastikin sulkeet ovat tasapainossa.
    # Esimerkiksi, jos merkkijono = "varis", niin sulkumerkit -listan pituus on 0,
    # koska merkkijonossa ei ole merkkejä ()[].
    # Siispä, jos sulkumerkit -listan pituus on 0, palautetaan True (sulkeet tasapainossa).
    if len(sulkumerkit) == 0:
        return True

    # Tarkistetaan, ovatko ensimmäinen ja viimeinen merkki joko "(" ja ")" tai "[" ja "]".
    # Jos ei (if not), niin palautetaan False (koska tällöin siis sulut eivät ole tasapainossa).
    # Huomaa, että sulut eivät saa mennä ristiin, eli esim. (] ei saa palauttaa True.
    # Tästä syystä siis täytyy tarkastaa erikseen tapaukset, jossa ensimmäinen ja viimeinen merkki ovat \
    # joko kaari- tai hakasulkeet.
    if not ((sulkumerkit[0] == "(" and sulkumerkit[-1] == ")") or (sulkumerkit[0] == "[" and sulkumerkit[-1] == "]")):
        return False

    # Poistetaan ensimmäinen ja viimeinen merkki.
    # Huomaa, että koska funktio sulut_tasapainossa odottaa argumentikseen merkkijonoa,
    # voidaan käyttää esim. join() -metodia, jolla saadaan sulkumerkit -listan merkit yhdistettyä merkkijonoksi.
    return sulut_tasapainossa("".join(sulkumerkit[1:-1]))


if __name__ == "__main__":

    x = sulut_tasapainossa("[(x)]")
    print(x)    # True

    y = sulut_tasapainossa("([(xyz))")
    print(y)    # False
