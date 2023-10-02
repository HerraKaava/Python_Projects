

class Tehtava:
    """ Luokka mallintaa ohjelmistoyritykselle annettavia työtehtäviä """

    # Luokkamuuttujia eli staattisia muuttujia käytetään luokan kautta eikä luokasta muodostettujen olioiden kautta.
    # Luokkamuuttujalla on yksi yhteinen arvo riippumatta siitä, montako oliota luokasta muodostetaan.
    # Luokka muuttujan määrittely eroaa attribuutista siten, että se määritellään ilman self-aluketta.
    # Jos luokkamuuttujaa halutaan käyttää koko luokassa ja mahdollisesti luokan ulkopuoleltakin,
    # se tulee määritellä metodien ulkopuolella.

    # Tehtävien id on juokseva numero, joka alkaa arvosta 1
    # (ensimmäisenä luotava tehtävä saa id:n 1, seuraava id:n 2 jne).
    # Toteutetaan id luokkamuuttujana.
    id = 1

    # Konstruktori
    def __init__(self, kuvaus: str, koodari: str, tyomaara: int):
        self.kuvaus = kuvaus
        self.koodari = koodari
        self.tyomaara = tyomaara

        # Asetetaan kuitenkin luokan Tehtava olioille attribuutti, joka on luokkamuuttujan id arvo.
        # Tätä arvoa kutsutaan __str__ -metodin yhteydessä, jolloin jokaiselle tehtävällä on oma uniikki id.
        self.id = Tehtava.id
        # Nyt kasvatetaan luokkamuuttujan arvoa ykkösellä,
        # jolloin seuraavan tehtävän id on yhden suurempi kuin edeltäjänsä.
        Tehtava.id += 1

        # Koska tehtävä ei ole siinä vaiheessa valmis, kun se luodaan,
        # alustetaan valmis -muuttuja, jonka arvoksi asetetaan False.
        # Huomaa, että on_valmis() -metodi palauttaa tämän muuttujan.
        self.valmis = False


    # Tehtävän tilan voi tarkistaa tällä metodilla, joka palauttaa totuusarvon.
    def on_valmis(self):
        # Palautetaan konstruktorissa luotu valmis -muuttuja, joka on totuusarvo.
        # Mikäli merkkaa_valmiiksi() -metodia ei ole kutsuttu oliossa,
        # niin valmis -muuttujan arvo on False.
        return self.valmis


    # Tehtävän voi merkata valmiiksi kutsumalla tätä metodia.
    def merkkaa_valmiiksi(self):
        # Tehtävä merkataan valmiiksi kutsumalla olion kautta tätä metodia,
        # eli tämän metodin ei tarvitse palauttaa mitään,
        # vaan ainoastaan muuttaa valmis -muuttujan arvo Trueksi.
        # Huomaa, että jos luodaan olio t1 = Tehtava ja kutsutaan t1.merkkaa_valmiiksi(),
        # ja tämän jälkeen luodaan uusi olio t2 = Tehtava ja kutsutaan t2.on_valmis(),
        # niin tälle oliolle tehtävän tila on edelleen False (kesken),
        # koska metodikutsut ovat henkilökohtaisia olioille.
        # Ts. jos kutsutaan merkkaa_valmiiksi() -metodia kerran jollekin oliolle,
        # se ei muuta koko ohjelman tilaa, vaan ainoastaan sen olion tilaa.
        self.valmis = True


    # Huomaa, että luokkamuuttujia kutsutaan luokan kautta.
    def __str__(self):
        # Tallennetaan valmiuden_tila -muuttujaan tieto siitä, onko self.valmis True vai False
        # (eli onko työ valmis vai kesken).
        # Huomaa, että "if not self.valmis" on sama asia kuin "if self.valmis == False".
        if not self.valmis:
            valmiuden_tila = "EI VALMIS"
        else:
            valmiuden_tila = "VALMIS"

        return f"{self.id}: {self.kuvaus} ({self.tyomaara} tuntia), koodari {self.koodari} {valmiuden_tila}"


class Tilauskirja:
    # Konstruktori
    def __init__(self):
        self.tasks = []    # Lista, joka sisältää luokan Tehtava olioita.


    # Lisää tilauksen 'tasks' -listaan.
    def lisaa_tilaus(self, kuvaus: str, koodari: str, tyomaara: int):
        # Tilaukset tallennetaan sisäisesti Tehtava-olioina.
        self.tasks.append(Tehtava(kuvaus, koodari, tyomaara))


    # Palauttaa listana kaikki tilauskirjalla olevat tehtävät
    def kaikki_tilaukset(self):
        # Palautetaan tilaukset listakoosteen avulla.
        # Huomaa, että koska 'tasks' -lista sisältää luokan Tehtava olioita,
        # niiden tulostusmuoto määritetään luokan Tehtava __str__ -metodissa,
        # joten siitä ei tarvitse välittää täällä.
        return [t for t in self.tasks]


    # Palauttaa listana kaikki koodarit, joille on tehtävä tilauskirjassa.
    # Huomaa, että metodin palauttama lista ei sisällä yhtä koodaria useampaan kertaan,
    # vaikka hän olisi tehnyt useita tehtäviä.
    def koodarit(self):
        # Myös täällä voidaan hyödyntää listakoostetta.
        # Nyt halutaan ainoastaan koodarin nimi.
        # Tämä on helppo toteuttaa sillä, 'tasks' -lista sisältää luokan Tehtava olioita,
        # joilla on koodari -attribuutti, joka palauttaa koodarin nimen.
        # Sama koodari ei saa kuitenkaan esiintyä useaan kertaan, vaikka hän olisi toteuttanut useamman tehtävän.
        # Duplikaatit on helppo poistaa listalta siten, että muutetaan ensin lista set-tyyppiseksi (built-in function).
        # set siis tarkoittaa joukkoa, ja joukossa kutakin alkiota voi olla vain yksi kappale.
        # Tämän jälkeen set voidaan muuttaa takaisin listaksi, ja duplikaatit ovat kadonneet.

        # Lisätään ensin kaikki koodarit duplikaatteineen coders -listaan
        coders = [c.koodari for c in self.tasks]
        # Nyt poistetaan duplikaatit coders -listasta
        coders_no_duplicates = list(set(coders))

        # Tulostetaan uniikit koodarien nimet listakoosteen avulla
        return [x for x in coders_no_duplicates]


    # Metodi saa parametriksi tehtävän id:n ja merkkaa kyseisen tehtävän valmiiksi.
    # Jos parametria vastaavaa tilausta ei löydy, metodi tuottaa poikkeuksen ValueError.
    def merkkaa_valmiiksi(self, id: int):
        # 'tasks' -lista sisältää luokan Tehtava olioita,
        # joten niillä on luokan Tehtava metodi merkkaa_valmiiksi()
        # (saman niminen metodi kuin tämä, täällä siis kutsutaan luokan Tehtava merkkaa_valmiiksi() -metodia).
        # Koska kyseessä on lista, sitä voidaan indeksoida.
        # Pythonissa indeksointi alkaa nollasta, eli jos halutaan esim. merkata valmiiksi tehtävä,
        # jonka id=2, listasta täytyy indeksoida id-1
        # (joka palauttaa listan toisen alkion, eli Tehtava-olion, jonka id=2).

        indeksi = id-1
        # Tässä tuotetaan manuaalisesti list index out of range -virhe.
        # Eli jos tilausta ei löydy (indeksi liian suuri), annetaan virhe.
        if indeksi >= len(self.tasks):
            raise ValueError("Tilausta ei löydy")

        # Jos kaikki ok (id kunnossa eli tilaus löytyy), niin merkataan tilaus valmiiksi.
        self.tasks[id-1].merkkaa_valmiiksi()


    # Metodi tulostaa ne tilaukset, jotka ovat merkattu valmiiksi.
    def valmiit_tilaukset(self):
        # Palautetaan lista, johon filteröidään ne tilaukset 'tasks' -listasta,
        # joiden on_valmis() -metodi arvioituu totuusarvoksi True.
        # Huomaa, että ne tilaukset, joihin on kutsuttu merkkaa_valmiiksi() -metodi,
        # arvioituvat totuusarvoksi True.
        return [t for t in self.tasks if t.on_valmis()]


    # Metodi tulostaa ne tilaukset, jotka ovat vielä kesken.
    def ei_valmiit_tilaukset(self):
        # Palautetaan lista, niistä tilauksista, joiden on_valmis() -metodi arvioituu totuusarvoksi False
        # (näihin tilauksiin ei ole kutsuttu merkkaa_valmiiksi() -metodia).
        return [t for t in self.tasks if not t.on_valmis()]


    # Metodi kertoo koodarin valmistuneiden ja vielä valmistumattomien töiden määrän,
    # sekä näihin kuluneiden työtuntien summan.
    # Palautuksena saadaan tuple, joka on muotoa:
    # (valmistuneiden töiden lkm, valmistumattomien töiden lkm,
    # valmiiden töiden työmäärien summa, valmistumattomien töiden työmäärien summa).
    def koodarin_status(self, coder: str):
        # Koin tätä metodia tehdessäni oivalluksen siitä, kuinka tuo self -määre toimii!!! =))))
        # Metodin täytyy tarkistaa, onko parametrina annettu koodari ylipäätänsä tehnyt töitä.
        # Jos ei, niin metodi tuottaa poikkeuksen ValueError.
        # Tämä toiminnallisuus saadaan seuraavasti listakoosteen ja in -keywordin avulla:
        # Otetaan koodarien nimet talteen listaan ja tarkistetaan in -avainsanalla,
        # onko parametrina annettu koodari listassa.
        pythonistas = [x.koodari for x in self.tasks]
        if coder not in pythonistas:
            raise ValueError("Invalid coder")

        # Parametrina annetun koodarin valmiit työt.
        # self.valmiit_tilaukset() palauttaa listan kaikista valmistuneista tilauksista.
        # Tätä listaa on helppo filtteröidä siten,
        # että lasketaan ainoastaan ne työt, jossa koodarina on toiminut parametrina annettu coder.
        # Listakooste on tietenkin len() -funktion sisällä, koska halutaan valmiiden töiden lukumäärä.
        valmiit_lkm = len([x for x in self.valmiit_tilaukset() if x.koodari == coder])

        # Valmistumattomien töiden määrä saadaan samalla logiikalla ei_valmiit_tilaukset() -metodin avulla.
        ei_valmiit_lkm = len([x for x in self.ei_valmiit_tilaukset() if x.koodari == coder])

        # Valmiiden töiden summa.
        # Tämä saadaan listakoosteen avulla kutsumalla olion valmiit_tilaukset() -metodia,
        # joka palauttaa listan kaikista valmiista tilauksista.
        # Tämän jälkeen on helppo työ filteröidä listaa siten,
        # että lasketaan ainoastaan parametrina annetun koodarin valmiit tunnit.
        valmiit_tunnit = sum([x.tyomaara for x in self.valmiit_tilaukset() if x.koodari == coder])

        # Valmistumattomien töiden summa (sama logiikka kuin valmiiden tuntien listakoosteessa).
        valmistumattomat_tunnit = sum([x.tyomaara for x in self.ei_valmiit_tilaukset() if x.koodari == coder])

        # Huomaa, että return keyword palauttaa automaattisesti tuplen,
        # mikäli palautettavia objekteja on enemmän kuin 1 (sulkeita ei siis tarvita määrittämään tuplea).
        return valmiit_lkm, ei_valmiit_lkm, valmiit_tunnit, valmistumattomat_tunnit


if __name__ == "__main__":

    tilaukset = Tilauskirja()
    tilaukset.lisaa_tilaus("koodaa webbikauppa", "Antti", 10)
    tilaukset.lisaa_tilaus("tee mobiilisovellus työaikakirjanpitoon", "Antti", 25)
    tilaukset.lisaa_tilaus("tee ohjelma matematiikan harjoitteluun", "Antti", 100)
    tilaukset.lisaa_tilaus("tee uusi facebook", "Erkki", 1000)

    tilaukset.merkkaa_valmiiksi(1)
    tilaukset.merkkaa_valmiiksi(2)

    status = tilaukset.koodarin_status("Antti")
    print(status)


