

# Rekursiolla tarkoitetaan sitä, että funktio kutsuu itseään.
# Rekursiossa funktion parametrien pitää kuitenkin muuttua niin, että jossain vaiheessa kutsuminen lopetetaan.
# Perusperiaate on sama kuin silmukoissa: jotta silmukka ei jatkuisi ikuisesti, siinä tulee olla päättymisehto,
# joka toteutuu jossain vaiheessa.

# Tietojenkäsittelytieteteessä erotetaan usein iteratiiviset ja rekursiiviset algoritmit.
# Iteratiivinen tarkoittaa tapaa, jossa ratkaisu perustuu peräkkäisyyteen
# (yleensä siihen, että käsitellään rakenne silmukassa).
# Rekursiivinen tarkoittaa vaihtoehtoista tapaa,
# jossa funktio silmukan sijasta (tai lisäksi) kutsuu itseään muuttuvilla parametrien arvoilla.

def listaan_lukuja(luvut: list):
    """
    Funktio lisää parametrina annettuun listaan lukuja niin kauan, kunnes listan pituus on viidellä jaollinen.
    Jokainen listaan lisättävä uusi luku on aina yhden suurempi kuin listan viimeinen luku.
    """
    if len(luvut) % 5 != 0:
        luvut.append(luvut[-1]+1)
        # Rekursiivinen kutsu
        listaan_lukuja(luvut)


if __name__ == "__main__":

    nums = [1, 3, 4, 5, 10, 11]
    listaan_lukuja(nums)
    print(nums)         # [1, 3, 4, 5, 10, 11, 12, 13, 14, 15]
                        #   --> koska nyt lukuja 10 (jaollinen viidellä), rekursiivinen algoritmi lopetettiin.

    